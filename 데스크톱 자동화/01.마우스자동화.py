import pyautogui
import time
#1. 화면크기 측정하기
print(pyautogui.size())

# time.sleep(2)

#2. 마우스 위치 측정하기
print(pyautogui.position())  #이거 대신 02.마우스 정보2를 이용하면 편함

#3. 마우스 이동
pyautogui.moveTo(40, 306, 2)

#4. 마우스 클릭
pyautogui.click()
pyautogui.click(button = 'right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데, 1초마다 하라고 하셈

#5. 마우스 드래그
pyautogui.moveTo(467,58, 2)  #초기 위치 잡기
pyautogui.dragTo(708,63, 2)  #초기 위치에서 해당 좌표로 드래그 함