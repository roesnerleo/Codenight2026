import pyautogui
import math

faust = 0
zeigefinger = 0
links = 0
oben = 0
unten = 0
rechts = 0

# ---------- Gestenerkennung ----------
def extended(hand, t, k):
    # t = Fingerspitze, k = Mittelgelenk, hand[0] = Handgelenk
    # Gestreckt = Spitze ist weiter vom Handgelenk entfernt als das Mittelgelenk
    return (math.hypot(hand[t].x - hand[0].x, hand[t].y - hand[0].y) >
            math.hypot(hand[k].x - hand[0].x, hand[k].y - hand[0].y))

def direction(hand, t, k):
    # t = Fingerspitze, k = Mittelgelenk, hand[0] = Handgelenk
    # Gestreckt = Spitze ist weiter vom Handgelenk entfernt als das Mittelgelenk
    if ((hand[t].x - hand[3].x) < 0 and math.fabs(hand[t].x - hand[3].x) > math.fabs(hand[t].y - hand[3].y)):
        return "left"
    if ((hand[t].x - hand[3].x) > 0 and math.fabs(hand[t].x - hand[3].x) > math.fabs(hand[t].y - hand[3].y)):
        return "right"
    if ((hand[t].y - hand[3].y) < 0 and math.fabs(hand[t].x - hand[3].x) < math.fabs(hand[t].y - hand[3].y)):
        return "up"
    if ((hand[t].y - hand[3].y) > 0 and math.fabs(hand[t].x - hand[3].x) < math.fabs(hand[t].y - hand[3].y)):
        return "down"   


def detect_gesture(hand):
    global faust, zeigefinger, links, rechts, oben, unten
    # Vier Ja/Nein-Werte: ist der Finger gestreckt?
    index  = extended(hand, 8, 6)
    middle = extended(hand, 12, 10)
    ring   = extended(hand, 16, 14)
    pinky  = extended(hand, 20, 18)
    thumb  = extended(hand, 4, 3)

    if index and not (middle or ring or pinky):
        if zeigefinger == 0:
            pyautogui.press('q')
            zeigefinger = 1
        return "Zeigefinger"          # nur der Zeigefinger
    else:
        zeigefinger = 0
    if middle and not (index or ring or pinky):
        pyautogui.click()
        return "Mittelfinger"         # nur der Mittelfinger
    if not (index or middle or ring or pinky or thumb):
        if faust == 0:
            pyautogui.press('e')
            faust = 1
        return "Faust"                # alle eingeklappt
    else:
        faust = 0
    if index and middle and ring and pinky:
        return "Offene Hand"          # alle gestreckt
    if thumb and not (index or middle or ring or pinky):
        match direction(hand, 4, 3):
            case "left":
                pyautogui.keyUp('d')
                pyautogui.keyUp('w')
                pyautogui.keyUp('s')
                rechts = 0
                oben = 0
                unten = 0
                if links == 0:
                    pyautogui.keyDown('a')
                    links = 1
                return "Daumen links"      # nur der Daumen nach links
            case "right":
                pyautogui.keyUp('a')
                pyautogui.keyUp('w')
                pyautogui.keyUp('s')
                links = 0
                oben = 0
                unten = 0
                if rechts == 0:
                    pyautogui.keyDown('d')
                    rechts = 1
                return "Daumen rechts"     # nur der Daumen nach rechts
            case "up":
                pyautogui.keyUp('s')
                pyautogui.keyUp('a')
                pyautogui.keyUp('d')
                links = 0
                rechts = 0
                unten = 0
                if oben == 0:
                    pyautogui.keyDown('w')
                    oben = 1
                return "Daumen oben"       # nur der Daumen nach oben
            case "down":
                pyautogui.keyUp('w')
                pyautogui.keyUp('a')
                pyautogui.keyUp('d')
                links = 0
                rechts = 0
                oben = 0
                if unten == 0:
                    pyautogui.keyDown('s')
                    unten = 1
                return "Daumen unten"      # nur der Daumen nach unten
            case _:
                return "Daumen"               # nur der Daumen
    if index and middle and not (ring or pinky):
        return None                       # alles andere ignorieren

