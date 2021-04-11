import cv2
import numpy as np

img = cv2.imread("Resources/opencv.jpg")

imgHor = np.hstack((img,img))
print(imgHor)

cv2.imshow("Horizontal", imgHor)

cv2.waitKey(0)