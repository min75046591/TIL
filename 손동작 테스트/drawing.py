import cv2
import mediapipe as mp
import numpy as np

# MediaPipe 손 인식 모듈 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 웹캠 초기화
cap = cv2.VideoCapture(0)

# 손 인식 모델 실행
with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:  # max_num_hands=2로 설정
    canvas = None
    prev_points = {'Right': (None, None), 'Left': (None, None)}  # 각각의 손끝 좌표를 저장
    prev_wrist_x = {'Right': None, 'Left': None}  # 오른손과 왼손의 손목 좌표

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("웹캠에서 프레임을 읽을 수 없습니다.")
            break

        # 캔버스 초기화 (프레임 크기와 동일)
        if canvas is None:
            canvas = np.zeros_like(frame)

        # 좌우 반전 및 BGR -> RGB 변환
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # 손이 감지되었을 때
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                # 오른손과 왼손 구분
                hand_label = handedness.classification[0].label  # 'Right' 또는 'Left'

                # 랜드마크 좌표를 프레임 크기에 맞게 변환
                h, w, _ = frame.shape
                landmarks = [(int(landmark.x * w), int(landmark.y * h)) for landmark in hand_landmarks.landmark]

                # 검지 손가락만 펴져 있는지 확인
                index_finger_extended = (
                    landmarks[8][1] < landmarks[6][1] and  # 검지 끝이 아래 마디보다 위에 있을 때
                    landmarks[6][1] < landmarks[5][1]  # 검지 아래 마디가 손바닥 쪽보다 위에 있을 때
                )

                # 다른 손가락이 모두 접혀 있는지 확인
                other_fingers_folded = (
                    landmarks[10][1] > landmarks[9][1] and  # 중지 접힘 확인
                    landmarks[14][1] > landmarks[13][1] and  # 약지 접힘 확인
                    landmarks[18][1] > landmarks[17][1]  # 새끼 접힘 확인
                )

                # 검지만 펴져 있을 때만 그림을 그림
                if index_finger_extended and other_fingers_folded:
                    x, y = landmarks[8]  # 검지 손끝 좌표

                    # 이전 좌표가 존재할 때만 선을 그림
                    if prev_points[hand_label][0] is not None and prev_points[hand_label][1] is not None:
                        cv2.line(canvas, prev_points[hand_label], (x, y), (255, 0, 0), 5)

                    # 현재 좌표를 이전 좌표로 업데이트
                    prev_points[hand_label] = (x, y)
                else:
                    # 조건이 맞지 않으면 그리기 중지
                    prev_points[hand_label] = (None, None)

                # 슬라이드 동작 감지 (손바닥이 오른쪽에서 왼쪽으로 이동)
                wrist_x = landmarks[0][0]  # 손목 x 좌표
                if prev_wrist_x[hand_label] is not None:
                    if prev_wrist_x[hand_label] - wrist_x > 30:  # 이전보다 30픽셀 이상 왼쪽으로 이동하면 슬라이드로 판단
                        canvas = np.zeros_like(frame)  # 캔버스 초기화
                        print(f"{hand_label} 캔버스 초기화!")

                # 손목 좌표 업데이트
                prev_wrist_x[hand_label] = wrist_x

                # 랜드마크를 프레임에 그림 (디버깅용)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        else:
            # 손이 감지되지 않으면 이전 좌표 초기화
            prev_points = {'Right': (None, None), 'Left': (None, None)}
            prev_wrist_x = {'Right': None, 'Left': None}

        # 프레임에 캔버스를 덧씌우는 방식 수정
        output = frame.copy()  # 원본 프레임 복사
        output[canvas > 0] = canvas[canvas > 0]  # 캔버스의 픽셀이 있는 부분만 덧씌움


        # 결과 화면 출력
        cv2.imshow('Finger Drawing', output)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# 종료
cap.release()
cv2.destroyAllWindows()
