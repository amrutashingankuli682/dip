import numpy as np
import matplotlib.pyplot as plt 
from skimage import io

# Load the RGB image 
image = io.imread('dedw.jpg')

def histogram_equalization_rgb(image):
# Create an empty array to store the equalized channels 
  equalized_image = np.zeros_like(image)

# Process each channel independently
  for channel in range(3): # RGB channels: 0=Red, 1=Green, 2=Blue 
    flat_channel = image[:, :, channel].flatten()
    histogram = np.zeros(256) 
    for pixel in flat_channel:
     histogram[pixel] += 1


    cdf = np.zeros_like(histogram) 
    cdf[0] = histogram[0]
    for i in range(1, len(histogram)):
      cdf[i] = cdf[i - 1] + histogram[i]

    cdf_min = np.min(cdf[np.nonzero(cdf)]) 
    cdf_max = cdf[-1]
    equalized_values = np.zeros_like(cdf, dtype=np.uint8) 
    for i in range(len(cdf)):
      equalized_values[i] = round((cdf[i] - cdf_min) / (cdf_max - cdf_min) * 255)
      equalized_channel = np.array([equalized_values[pixel] for pixel in flat_channel], dtype=np.uint8)
      equalized_image[:, :, channel] = equalized_channel.reshape(image[:, :, channel].shape)
    return equalized_image

  # Perform histogram equalization on the RGB image equalized_image = histogram_equalization_rgb(image) # Display original and equalized images plt.figure(figsize=(12, 6))
  plt.subplot(1, 2, 1) 
  plt.title('Original RGB Image') 
  plt.imshow(image) 
  plt.axis('off')

  plt.subplot(1, 2, 2)
  plt.title('Equalized RGB Image (Manual)') 
  plt.imshow(equalized_image) 
  plt.axis('off')
  plt.tight_layout() 
plt.show()
