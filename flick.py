# flick vars
gate = 0.2
flickUp = 0
flickDown = 0
FlickLeft = 0
FlickRight = 0


def flickcheck(queue12):
    
    
    xDif = queue12[0][0] - queue12[1][0]
    yDif = queue12[0][1] - queue12[1][1]
    
    if yDif > gate:
        flickUp = 1
    else:
        flickUp = 0
    
    if yDif < -gate:
        flickDown = 1
    else:
        flickDown = 0
    
    if xDif > gate:
        flickLeft = 1
    else:
        flickLeft = 0
    
    if xDif < -gate:
        flickRight = 1
    else:
        flickRight = 0
    
    print("Up: " + str(flickUp))
    print("Down: " + str(flickDown))
    print("Left: " + str(flickLeft))
    print("Right: " + str(flickRight))
    return [flickUp, flickDown, flickLeft, flickRight]