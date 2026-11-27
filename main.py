import cv2
import mediapipe as mp
import time

# Webcam initialisieren
cap = cv2.VideoCapture(0)

while True:

    # get Cam Footage
    success, frame = cap.read()

    if not success:
        print("Error: Cam not working")
        break

    # flip Image 
    frame = cv2.flip(frame, 1)

    # Bild anzeigen
    cv2.imshow("Hand Tracking", frame)

    # close
    if cv2.waitKey(1) & 0xFF == ord('esc'):
        break

# Ressourcen freigeben
cap.release()
cv2.destroyAllWindows()