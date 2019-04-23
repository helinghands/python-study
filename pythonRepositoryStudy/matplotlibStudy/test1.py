import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("1.jpg")
print(img)
imgplot = plt.imshow(img)
lum_img = img[:, :, 0]
plt.imshow(lum_img)
plt.show()