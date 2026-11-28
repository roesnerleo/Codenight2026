import cv2
import mediapipe as mp
import time
import math
import flick

# Inizialize Cam
cap = cv2.VideoCapture(0)

# config MediaPipe
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


# ModelPath
MODEL_PATH = "models/hand_landmarker.task"

# Connections between HandMarks
CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17)
]

#Counter for detection over time
counter = 0

# queue Point 12
queue12 = [[0, 0],[0, 0]]

# reset var for ready check
ready = False


                    

# Settings 
options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=MODEL_PATH
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1
)

# start Tracking
with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = cap.read()

        if not success:
            break

        # flip Image
        frame = cv2.flip(frame, 1)

        # convert Colors from BGR zu RGB 
        rgb_frame = cv2.cvtColor(
            frame, cv2.COLOR_BGR2RGB
        )

        # get MediaPipe-Image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # get Hands
        timestamp_ms = int(time.monotonic() * 1000)

        result = landmarker.detect_for_video(
            mp_image,
            timestamp_ms
        )

        # get results from Hands
        if result.hand_landmarks:

            for hand in result.hand_landmarks:

                height, width, _ = frame.shape

                # get Coordinates from Marks
                points = []

                for landmark in hand:
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)
                    points.append((x, y))

                # draw Connections
                for start, end in CONNECTIONS:
                    cv2.line(
                        frame,
                        points[start],
                        points[end],
                        (0, 255, 0),
                        2
                    )

                # Draw Marks
                for point in points:
                    cv2.circle(
                        frame,
                        point,
                        5,
                        (0, 0, 255),
                        -1
                    )

        # show Image
        cv2.imshow("MediaPipe Hand Tracking", frame)

        # ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break


        if result.hand_landmarks:

            for hand in result.hand_landmarks:

                # read Mark Coordinates
                landmark = hand[12]
        

                if counter == 0:

                    queue12[0] = queue12[1]
                    queue12[1] = [round(landmark.x, 3), round(landmark.y, 3)]
                    flick.flickcheck(queue12)   

            pass

        else:
            pass
           # print("noHandFound")


        # count
        if counter < 1:
            counter += 1
        else: 
            counter = 0



# release resources
cap.release()
cv2.destroyAllWindows()