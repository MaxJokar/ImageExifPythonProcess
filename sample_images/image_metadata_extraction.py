# Install exif Package
# Import Dependencies
# View Sample Image
# Open image as exif Image
# Read and Explore Metadata
# Modify Metadata
# Save Image with Modified Metadata


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

import cv2
from exif import Image


# Define image path
folder_path = 'sample_images'
img_filename = 'image_1.jpg'
img_path = f'{folder_path}/{img_filename}'


# View Sample Image
img = cv2.imread(img_path)
print(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img)

plt.rcParams["figure.figsize"] = (20,10)


plt.axis('off')
print(plt.imshow(img))




