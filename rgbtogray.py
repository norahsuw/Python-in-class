import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

bb_RGB=cv2.imread("bb.jpg")
bb_gray=cv2.cvtColor(bb_RGB,cv2.COLOR_BGR2GRAY)#轉灰階
bb_pseudo=cv2.cvtColor(bb_gray,cv2.COLOR_GRAY2RGB)
#cv2. imshow("RGB",bb_RGB)
cv2. imshow("Gray" ,bb_gray)
#cv2. imshow("Pseudo",bb_pseudo)

bb_index=bb_gray/64 #用64切
mycolormap=ListedColormap([[0,0.7,0.6],[1,0.5,0.5],[1,0.1,0.3],[0.4,0.1,0.1]])#rgb
plt.imshow(bb_gray,cmap=mycolormap)

N=30#切30份
fig2=plt.figure(2)
colors=[(r,g,b)for(r,g,b)in zip(np.linspace(0.2,1,N),np.linspace(0.3,0,N),np.linspace(0,0.9,N))]#比例
my_cmap=mpl.colors.ListedColormap(colors)

plt.imshow(bb_gray,cmap=my_cmap)
cv2.waitKey()
cv2.destroyAllWindows()