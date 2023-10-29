import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread('img.jpg')

kernal=np.array([[5,0,0,0,-5],
                 [5,0,0,0,-5],
                 [5,0,1,0,-5],
                 [5,0,0,0,-5],
                 [5,0,0,0,-5]])

kernal1=np.array([[-5,0,0,0,5],
                 [5,0,0,0,-5],
                 [0,0,1,0,0],
                 [-5,0,0,0,5],
                 [5,0,0,0,-5]])



dst = cv2.filter2D(image, -1, kernal)
dst1 = cv2.filter2D(image, -1, kernal1)

#plt.subplot(121) 
#plt.title("Original")
#plt.imshow(image[...,::-1])
plt.subplot(122) 
plt.title("Changed")
plt.imshow(image[...,::-1])
plt.subplot(121) 
plt.title("Changed1")
plt.imshow(dst[...,::-1])


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

