import cv2
import mediapipe as mp

# MediaPipe의 손 인식 모듈 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 손 제스처 상태 초기화
is_fist_detected = False  # 주먹이 쥐어진 상태를 확인
landmarks_visible = False  # 랜드마크 표시 여부

# 웹캠 시작 (0번 카메라)
cap = cv2.VideoCapture(0)

# 비디오 녹화 초기화
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# 손 인식 모델 실행
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("웹캠에서 프레임을 읽을 수 없습니다.")
            break

        # 좌우 반전 및 BGR을 RGB로 변환
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # 손이 감지되었을 때
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 랜드마크 좌표 계산
                h, w, _ = frame.shape
                landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]

                # 주먹 쥔 상태 감지
                fingers_folded = (
                    landmarks[8][1] > landmarks[6][1] and  # 검지가 접힘
                    landmarks[12][1] > landmarks[10][1] and  # 중지가 접힘
                    landmarks[16][1] > landmarks[14][1] and  # 약지가 접힘
                    landmarks[20][1] > landmarks[18][1]  # 새끼가 접힘
                )

                if fingers_folded and not landmarks_visible:  # 주먹 쥔 상태 확인
                    is_fist_detected = True

                if is_fist_detected and not fingers_folded:  # 주먹을 폈을 때 랜드마크 표시
                    landmarks_visible = True
                    is_fist_detected = False  # 상태 초기화

                # 랜드마크 표시가 활성화된 경우에만 화면에 출력
                if landmarks_visible:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        else:
            # 손이 감지되지 않으면 랜드마크 표시 초기화
            landmarks_visible = False

        # 비디오 녹화
        out.write(frame)

        # 웹캠 화면 출력
        cv2.imshow('MediaPipe Hands', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# 웹캠 및 비디오 녹화 해제
cap.release()
out.release()
cv2.destroyAllWindows()
