import numpy as np
import cv2

# Read the image
im = cv2.imread("examples/apple_88.jpg", 1)

# Use predefined gaussian filter with rgb values - would be too complex to do it myself
im_gaussian = cv2.GaussianBlur(im, (1, 1), 0)
im_gaussian = np.clip(im_gaussian, 0, 255)

# Define the Laplacian kernel
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Apply the Laplacian filter
im_laplace = cv2.filter2D(im_gaussian, -1, kernel)
im_laplace = cv2.convertScaleAbs(im_laplace)

# Save the filtered image
cv2.imwrite("examples/laplace.jpg", im_laplace)
