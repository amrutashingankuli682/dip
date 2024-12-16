import matplotlib.pyplot as plt 
import numpy as np
import cv2
 
 
image = cv2.imread("dedw.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Pixelate 
pixel_size = 10
small_image = image[::pixel_size, ::pixel_size, :]
pixelated_image = np.repeat(np.repeat(small_image, pixel_size, axis=0), pixel_size, axis=1)

# Blur 
kernel_size = 5
blurred_image = np.zeros_like(image)
padded_image = np.pad(image, ((kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2), (0, 0)), mode='edge')
for i in range(image.shape[0]): 
  for j in range(image.shape[1]):
    for k in range(3):
      blurred_image[i, j, k] = np.mean(padded_image[i:i+kernel_size, j:j+kernel_size,
k])

# Add Noise
noise = np.random.randint(0, 50, image.shape, dtype=np.uint8) 
noisy_image = np.clip(image + noise, 0, 255)

plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1) 
plt.title("Original Image") 
plt.imshow(image) 
plt.axis("off")

plt.subplot(2, 2, 2) 
plt.title("Pixelated Image") 
plt.imshow(pixelated_image)
 
 
plt.axis("off")

plt.subplot(2, 2, 3) 
plt.title("Blurred Image") 
plt.imshow(blurred_image) 
plt.axis("off")

plt.subplot(2, 2, 4) 
plt.title("Noisy Image") 
plt.imshow(noisy_image) 
plt.axis("off")

plt.tight_layout() 
plt.show()
