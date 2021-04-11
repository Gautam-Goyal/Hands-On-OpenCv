import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
# img[:]=255,0,0 # OR [255,0,0]
# print(img)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #shape[1]=height, shape[0]=width
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(320,200),120,(255,0,0),20)
cv2.putText(img,"OPEN CV",(200,400),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,150,200),4)

cv2.imshow("Image",img)
cv2.waitKey(0)

"""
Breaking/Splitting the image in 3 different channels (B,G,R)
BY SHOWING THE IMAGE USING imshow IT WILL BE VISIBLE IN GRAYSCALE
THEREFORE TO SHOW THE IMAGE COLOURFUL /BGR FORMAT ,ONLY ONE CHANNEL
SHOULD BE DISPLAYED WITH OTHER 2 CHANNELS MADE ZERO
"""
# import numpy as np
# import cv2
#
# image = np.random.rand(200, 200, 3)
# b, g, r = cv2.split(image)
# cv2.imshow('green', g)
# cv2.waitKey(0)
#
# black = np.zeros((200, 200, 3))
# black[:, :, 1] = g  # Set only green channel
# cv2.imshow('green', black)
# cv2.waitKey(0)
'''
If we look to a pixel in the blue rectangle of the original colored image, 
it will have the value of the blue channel equal to 255 and the remaining ones equal to 0: (B=255, G=0, R=0).

So, if we display the blue channel image in a window, this pixel will be equal to 255
and since it is a grayscale image, it corresponds to white. 
For the Green and Red channel images, this pixel will be equal to 0 
and since it is a grayscale image, it corresponds to black.

This is why, in the blue channel image, we see a white rectangle where 
on the original image was a Blue rectangle. In the other channel images, 
we see black in that area.

'''
# import cv2
# import numpy
#
# img = cv2.imread('C:/Users/N/Desktop/bgr.png')
#
# blue, green, red = cv2.split(img)
#
# zeros = numpy.zeros(blue.shape, numpy.uint8)
#
# blueBGR = cv2.merge((blue, zeros, zeros))
# greenBGR = cv2.merge((zeros, green, zeros))
# redBGR = cv2.merge((zeros, zeros, red))
#
# cv2.imshow('blue BGR', blueBGR)
# cv2.imshow('green BGR', greenBGR)
# cv2.imshow('red BGR', redBGR)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()