import pyautogui
def convert(results):
    if results[0] == 1:
        pyautogui.press('w')
    if results[1] == 1:
        pyautogui.press('a')
    if results[2] == 1:
        pyautogui.press('s')
    if results[3] == 1:
        pyautogui.press('d')
    if results[4] == 1:
        pyautogui.press('e')
    if results[5] == 1:
        pyautogui.press('q')
    if results[6] == 1:
        pyautogui.keyDown('w')
    else:
        pyautogui.keyUp('w')
    if results[7] == 1:
        pyautogui.keyDown('a')
    else:
        pyautogui.keyUp('a')
    if results[8] == 1:
        pyautogui.keyDown('s')
    else:
        pyautogui.keyUp('s')
    if results[9] == 1:
        pyautogui.keyDown('d')
    else:
        pyautogui.keyUp('d')