import numpy as np
import cv2

# Read the image
im = cv2.imread("examples/apple_94.jpg", 1)

# use predefined gaussian filter with rgb values - would be too complex to do it myself
im_gaussian = cv2.GaussianBlur(im, (3, 3), 0)
im_gaussian = np.clip(im_gaussian, 0, 255)

# Define the Sobel kernels
kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Apply the Sobel filter
im_x = cv2.filter2D(im_gaussian, -1, kernel_x)
im_y = cv2.filter2D(im_gaussian, -1, kernel_y)
im_x = cv2.convertScaleAbs(im_x)
im_y = cv2.convertScaleAbs(im_y)
im_sobel = cv2.addWeighted(im_x, 0.5, im_y, 0.5, 0)

# Save/Show the filtered image
cv2.imwrite("examples/sobel.jpg", im_sobel)
