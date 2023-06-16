import cv2
import pyautogui
# import numpy
from win32api import GetSystemMetrics
import numpy as np
import time

# to cover whole screen in recording
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width,height)

# to make format like .mp4 of video
f = cv2.VideoWriter_fourcc(*"XVID")

# to save the video
output = cv2.VideoWriter("test.mp4",f,30.0,dim)

# add current timing and how much time want to record the screen
now_start_time = time.time()
dur = 10+4
end_time = now_start_time+dur

# to record the screen
while True:
  # take scrrenshot of screen
  image = pyautogui.screenshot()
  # make screenshot in form of frame and make video
  frame_1 = np.array(image)
  # give originalcolor to recorded video
  frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

  output.write(frame)
  # at which time video should be end
  c_time = time.time()
  if c_time > end_time:
    break

# to release the video
output.release()
print("--END--")
