import matplotlib.pyplot as plt 
import numpy as np
import cv2

image = cv2.imread("dedw.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]

hist_R = np.zeros(256, dtype=int) 
hist_G = np.zeros(256, dtype=int) 
hist_B = np.zeros(256, dtype=int)

for value in R.flatten(): hist_R[value] += 1
for value in G.flatten(): hist_G[value] += 1
for value in B.flatten(): hist_B[value] += 1

plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1) 
plt.title("Image") 
plt.imshow(image) 
plt.axis("off")

plt.subplot(2, 2, 2) 
plt.title("Red Histogram")
plt.bar(range(256), hist_R, color='red', width=1) 
plt.xlabel("Pixel Value")
 
 
plt.ylabel("Frequency")

plt.subplot(2, 2, 3) 
plt.title("Green Histogram")
plt.bar(range(256), hist_G, color='green', width=1) 
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4) 
plt.title("Blue Histogram")
plt.bar(range(256), hist_B, color='blue', width=1) 
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")


plt.tight_layout() 
plt.show()
