import cv2
import numpy as np

img = cv2.imread("Resources/opencv.jpg")
print(img.shape)  # --> (227, 223, 3) - Height, Width, ID or channel no. for image type i.e. BGR here

imgResize = cv2.resize(img, (180, 200))  # Width ,Height
imgCropped = img[0:180, 100:200]  # Height,Width

kernel = np.ones((5, 5), np.uint8)
print(kernel)
# print("\nMatrix a : \n", kernel) OpenCV blurs an image by applying what's called a Kernel. A Kernel tells you how
# to change the value of any given pixel by combining it with different amounts of the neighboring pixels. The kernel
# is applied to every pixel in the image one-by-one to produce the final image (this operation known as a convolution).

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgblur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=4)
# Iterations =No of times the dilation applied

imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDilation)
cv2.imshow("Erosion Image", imgEroded)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)

# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,10)
#
# while True:
#     success,img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
