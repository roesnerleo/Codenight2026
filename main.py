import cv2

# Webcam initialisieren
cap = cv2.VideoCapture(0)

while True:

    # Einzelnes Kamerabild aufnehmen
    success, frame = cap.read()

    if not success:
        print("Kamera konnte nicht geöffnet werden!")
        break

    # Bild spiegeln
    frame = cv2.flip(frame, 1)

    # Bild anzeigen
    cv2.imshow("Hand Tracking", frame)

    # Beenden mit Taste Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Ressourcen freigeben
cap.release()
cv2.destroyAllWindows()