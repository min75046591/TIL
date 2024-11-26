import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import numpy as np
from matplotlib import pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


# BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    if result is not None:
        print('gesture recognition result: {}'.format(result))
        # display_batch_of_images_with_gestures_and_hand_landmarks(images, results)
    else:
        cv2.putText(output_image, 'No gesture recognized', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Create the options for the gesture recognizer
base_options = python.BaseOptions(
    model_asset_path='gesture_recognizer.task'
)
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
)
recognizer = vision.GestureRecognizer.create_from_options(options)
frame_timestamp_ms = int(round(time.time() * 5000))

# Initialize the webcam
cap = cv2.VideoCapture(0)
timestamp = 0

with GestureRecognizer.create_from_options(options) as recognizer:
# The detector is initialized. Use it here.

# Create the gesture recognizer
# Send live image data to perform gesture recognition.
# The results are accessible via the `result_callback` provided in
# the `GestureRecognizerOptions` object.
# The gesture recognizer must be created with the live stream mode.

    # Initialize the webcam
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Ignoring empty frame")
            break

        timestamp += 1
        
    # Use OpenCV’s VideoCapture to start capturing from the webcam.
    # Create a loop to read the latest frame from the camera using VideoCapture#read()
    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

        # Send live image data to perform gesture recognition
        recognizer.recognize_async(mp_image, timestamp)

        cv2.imshow("MediaPipe Model", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()