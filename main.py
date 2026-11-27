import cv2
import mediapipe as mp
import time

# Inizialize Cam
cap = cv2.VideoCapture(0)

# config MediaPipe
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

while True:

    # get Cam Footage
    success, frame = cap.read()

    if not success:
        print("Error: Cam not working")
        break

    # flip Image 
    frame = cv2.flip(frame, 1)

    # show Image
    cv2.imshow("Hand Tracking", frame)

    # close
    if cv2.waitKey(1) & 0xFF == ord('esc'):
        break

# release Recources
cap.release()
cv2.destroyAllWindows()