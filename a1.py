import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
image_path = "dedw.jpg"
image = Image.open(image_path) 
rgb_image = np.array(image)
R = rgb_image[:, :, 0]
G = rgb_image[:, :, 1]
B = rgb_image[:, :, 2]
grayscale_image = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1) 
plt.title("Red Channel") 
plt.imshow(R, cmap="Reds")

plt.subplot(2, 2, 2) 
plt.title("Green Channel") 
plt.imshow(G, cmap="Greens")

plt.subplot(2, 2, 3) 
plt.title("Blue Channel") 
plt.imshow(B, cmap="Blues")

plt.subplot(2, 2, 4)
plt.title("Grayscale Image (Luminosity Method)") 
plt.imshow(grayscale_image, cmap="gray")

plt.tight_layout() 
plt.show()
