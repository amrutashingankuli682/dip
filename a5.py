import matplotlib.pyplot as plt 
import numpy as np
import cv2


image = cv2.imread("dedw.jpg")
image = 0.2989 * image[:, :, 2] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 0] 
mage = image.astype(np.uint8)

negative_image = 255 - image


histogram = np.zeros(256, dtype=int)
 
 
for value in image.flatten(): 
  histogram[value] += 1

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1) 
plt.title("Original Image") 
plt.imshow(image, cmap="gray") 
plt.axis("off")

plt.subplot(1, 2, 2) 
plt.title("Negative Image")
plt.imshow(negative_image, cmap="gray") 
plt.axis("off")

plt.tight_layout() 
plt.show()
