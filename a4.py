import matplotlib.pyplot as plt 
import numpy as np
import cv2


image = cv2.imread("dedw.jpg")
image = 0.2989 * image[:, :, 2] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 0] 
image = image.astype(np.uint8)

histogram = np.zeros(256, dtype=int) 
for value in image.flatten():
  histogram[value] += 1
 
 

plt.figure(figsize=(8, 6)) 
plt.title("Histogram for Grayscale Image")
plt.bar(range(256), histogram, color='gray', width=1, fill=False) 
plt.xlabel("Pixel Value")
plt.ylabel("Frequency") 
plt.show()
