import pyautogui
import math

faust = 0
zeigefinger = 0
pressKey = False

# ---------- Gestenerkennung ----------
def extended(hand, t, k):
    # t = Fingerspitze, k = Mittelgelenk, hand[0] = Handgelenk
    # Gestreckt = Spitze ist weiter vom Handgelenk entfernt als das Mittelgelenk
    return (math.hypot(hand[t].x - hand[0].x, hand[t].y - hand[0].y) >
            math.hypot(hand[k].x - hand[0].x, hand[k].y - hand[0].y))

#def direction(hand, t, k):
#    p = hand[t]
#    q = hand[3]
#    dx = p.x - q.x
#    dy = p.y - q.y
#    if dx * dx > dy * dy:
#        return "left" if dx < 0 else "right"
#    return "up" if dy < 0 else "down"


def detect_gesture(hand):
    global faust, zeigefinger, pressKey
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
    else:
        zeigefinger = 0
    if not (index or middle or ring or pinky or thumb):
        if faust == 0:
            pyautogui.press('e')
            faust = 1
    else:
        faust = 0
    #if thumb and not (index or middle or ring or pinky):
    #    dir = direction(hand, 4, 3)

    #    if dir == "left":
    #        if not pressKey:
    #            pyKey.pressKey('a')   # nur der Daumen nach links
    #            pressKey = True
    #    else:
    #        pyKey.releaseKey('a')
    #        pressKey = False

    #    if dir == "right":
    #        if not pressKey:
    #            pyKey.pressKey('d')  # nur der Daumen nach rechts
    #            pressKey = True
    #    else:
    #        pyKey.releaseKey('d')
    #        pressKey = False

    #    if dir == "up":
    #        if not pressKey:
    #            pyKey.pressKey('w')       # nur der Daumen nach oben
    #            pressKey = True
    #    else:
    #        pyKey.releaseKey('w')
    #        pressKey = False

    #    if dir == "down":
    #        if not pressKey:
    #            pyKey.pressKey('s')   # nur der Daumen nach unten
    #            pressKey = True
    #    else:
    #        pyKey.releaseKey('s')
    #        pressKey = False

    #elif pressKey:
    #    pyKey.releaseKey('d')
    #    pyKey.releaseKey('w')
    #    pyKey.releaseKey('a')
    #    pyKey.releaseKey('s')
    #    pressKey = False


