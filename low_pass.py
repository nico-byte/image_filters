import numpy as np
import cv2


## Low-Pass Filter
def low_pass_filter(img, size):
    # Create the filter
    filter_ = np.ones((size, size)) / (size**2)

    # Create the output image
    filtered_img = np.zeros_like(img)

    # Apply the filter
    for i in range(img.shape[0] - size):
        for j in range(img.shape[1] - size):
            filtered_img[i, j] = np.sum(img[i:i+size, j:j+size] * filter_)
    return filtered_img

# Example usage:
im = cv2.imread("examples/apple_95.jpg", 0)
im_low_pass = low_pass_filter(im, 10)
cv2.imwrite("examples/low_pass.jpg", im_low_pass)
