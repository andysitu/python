import pyautogui, time

time.sleep(5)
pyautogui.click()
distance1, dur = (200, 0.2)

while distance1 > 0:
    # move right
    pyautogui.dragRel(distance1, 0, dur)
    distance1 -= 5
    # move down
    pyautogui.dragRel(0, distance1, dur)
    # move left
    pyautogui.dragRel(-distance1, 0, dur)
    distance1 -= 5
    # move up
    pyautogui.dragRel(0, -distance1, dur)
