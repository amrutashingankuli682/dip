import matplotlib.pyplot as plt 
import numpy as np
import cv2

image = cv2.imread("dedw.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Linear Transformation
def linear_transform(img, alpha, beta):
  return np.clip(alpha * img + beta, 0, 255).astype(np.uint8) 
linear_image = linear_transform(image, 1.5, 20)
# Gamma Transformation
def gamma_transform(img, gamma):
  return np.clip(255 * (img / 255) ** gamma, 0, 255).astype(np.uint8)


gamma_image = gamma_transform(image, 2.2)
 

# Logarithmic Transformation 
def log_transform(img):
  c = 255 / np.log(1 + np.max(img))
  return np.clip(c * np.log(1 + img), 0, 255).astype(np.uint8) 
log_image = log_transform(image)
# Plot results plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1) 
plt.title("Original Image") 
plt.imshow(image) 
plt.axis("off")

plt.subplot(2, 2, 2) 
plt.title("Linear Transformation") 
plt.imshow(linear_image) 
plt.axis("off")

plt.subplot(2, 2, 3) 
plt.title("Gamma Transformation") 
plt.imshow(gamma_image) 
plt.axis("off")

plt.subplot(2, 2, 4) 
plt.title("Logarithmic Transformation") 
plt.imshow(log_image)
plt.axis("off")

plt.tight_layout() 
plt.show()
