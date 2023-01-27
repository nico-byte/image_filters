import numpy as np
import cv2

# Read the image
im = cv2.imread("examples/apple_88.jpg")

# Add padding to the image
im = np.pad(im, [(1, 1), (1, 1), (0, 0)], mode='constant')

# Create an empty image of the same size as the original image
im_median = np.zeros_like(im)

# Iterate over the rows and columns of the image
for row in range(1, im.shape[0] - 1):
    for col in range(1, im.shape[1] - 1):
        # Get the pixels in the kernel
        kernel = im[row - 1:row + 2, col - 1:col + 2]
        # Get the median value of the pixels in the kernel
        median = np.median(kernel)
        # Assign the median value to the corresponding pixel in the output image
        im_median[row, col] = median

# Remove the padding
im_median = im_median[1:-1, 1:-1]
# Save the filtered image
cv2.imwrite("examples/median.jpg", im_median)
