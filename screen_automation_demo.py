import pyautogui
import time

# activated accessibility to allow script to control comp
# lets open safari and see what we can do

# open search using command + space bar
pyautogui.keyDown('command')
pyautogui.keyDown('space')
pyautogui.keyUp('command')
pyautogui.keyUp('space')

# type in safari in the search box with a .25 ms delay per char
pyautogui.write('safari', interval=0.25)

# open safari by pressing enter
pyautogui.press('enter')

# wait 3 seconds for page to load
time.sleep(3)

# open youporn.com
pyautogui.write("youtube.com", interval=0.25)
pyautogui.press('enter')

# wait 3 seconds for page to load
time.sleep(3)

# tab tab then search
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('mitsubishi power systems', interval=0.25)
pyautogui.press('enter')

# wait 3 seconds for page to load
time.sleep(3)

# locate video i want to watch
x, y = pyautogui.locateCenterOnScreen('link.png', confidence=.8)

# div by 2 because retina display sucks
pyautogui.click(x/2, y/2)
