import pyautogui

# flick vars
gate = 0.2

flickUp = 0
flickDown = 0
flickLeft = 0
flickRight = 0


def flickcheck(queue12):

    global flickUp
    global flickDown
    global flickLeft
    global flickRight
    
    
    xDif = queue12[0][0] - queue12[1][0]
    yDif = queue12[0][1] - queue12[1][1]
    
    if yDif > gate:
        if flickUp == 0:
            flickUp = 1
            pyautogui.press('w')
    else:
        flickUp = 0
    
        if yDif < -gate:
            if flickDown == 0:
                flickDown = 1
                pyautogui.press('s')
        else:
            flickDown = 0
    
            if xDif > gate:
                if flickLeft == 0:
                    flickLeft = 1
                    pyautogui.press('a')
            else:
                flickLeft = 0
    
                if xDif < -gate:
                    if flickRight == 0:
                        flickRight = 1
                        pyautogui.press('d')
                else:
                    flickRight = 0
    
    print("Up: " + str(flickUp))
    print("Down: " + str(flickDown))
    print("Left: " + str(flickLeft))
    print("Right: " + str(flickRight))
    return [flickUp, flickDown, flickLeft, flickRight]