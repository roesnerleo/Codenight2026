import cv2
import mediapipe as mp
import time
import math
import gesten

# Kamera starten
cap = cv2.VideoCapture(0)

# MediaPipe konfigurieren
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Pfad zum Modell
MODEL_PATH = "models/hand_landmarker.task"

# Verbindungen zwischen den Hand-Punkten (für die grünen Linien)
CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17)
]



# Einstellungen
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1
)

# Tracking starten
with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = cap.read()
        if not success:
            break

        # Bild spiegeln
        frame = cv2.flip(frame, 1)

        # Farben von BGR nach RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # MediaPipe-Bild erzeugen
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Hände erkennen
        timestamp_ms = int(time.monotonic() * 1000)
        result = landmarker.detect_for_video(mp_image, timestamp_ms)

        # Ergebnisse auswerten
        if result.hand_landmarks:

            height, width, _ = frame.shape

            for n, hand in enumerate(result.hand_landmarks):

                # Koordinaten in Pixel umrechnen
                points = []
                for landmark in hand:
                    points.append((int(landmark.x * width), int(landmark.y * height)))

                # Verbindungen zeichnen
                for start, end in CONNECTIONS:
                    cv2.line(frame, points[start], points[end], (0, 255, 0), 2)

                # Punkte zeichnen
                for point in points:
                    cv2.circle(frame, point, 5, (0, 0, 255), -1)

                # Geste erkennen und ins Bild schreiben
                # (n * 40 sorgt dafür, dass bei zwei Händen die Texte untereinander stehen)
                gesture = gesten.ddetect_gesture(hand)
                print(gesture)
                cv2.putText(frame, str(gesture), (10, 40 + n * 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # Bild anzeigen
        cv2.imshow("MediaPipe Hand Tracking", frame)

        # ESC beendet das Programm
        if cv2.waitKey(1) & 0xFF == 27:
            break

# Aufräumen
cap.release()
cv2.destroyAllWindows()