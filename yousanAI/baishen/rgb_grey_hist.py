import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

filename=sys.argv[1]
img=cv2.imread(filename)
colors=['blue','green','red']

for i in range(3):
    hist,x=np.histogram(img[:,:,i].ravel(),bins=256,range=(0,256))
    plt.plot(0.5*(x[:-1]+x[1:]),hist,label=colors[i],color=colors[i])
plt.show()

imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('sample_gray.jpg',imggray)

histgray,xgray=np.histogram(imggray.ravel(),bins=256,range=(0,256))
plt.figure()
plt.plot(0.5*(xgray[:-1]+xgray[1:]),histgray)
plt.show()