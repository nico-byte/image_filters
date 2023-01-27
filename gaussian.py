import numpy as np
import cv2


## Gauß-Filter
def gaussian_filter(img, sigma):
    # Create the filter
    filter_size = int(6*sigma + 1)
    filter_size = filter_size + (1 - filter_size % 2)
    filter_ = np.zeros((filter_size, filter_size))
    center = filter_size//2
    for x in range(filter_size):
        for y in range(filter_size):
            filter_[x, y] = (1/(2*np.pi*sigma**2)) * np.exp(-((x-center)**2 + (y-center)**2)/(2*sigma**2))

    # Normalize the filter
    filter_ /= np.sum(filter_)

    # Create the output image
    filtered_img = np.zeros_like(img)

    # Apply the filter
    for i in range(img.shape[0] - filter_size):
        for j in range(img.shape[1] - filter_size):
            filtered_img[i, j] = np.sum(img[i:i+filter_size, j:j+filter_size] * filter_)
    return filtered_img

# Example usage:
im = cv2.imread("examples/apple_94.jpg", 0)
im_gauss = gaussian_filter(im, 1)
cv2.imwrite("examples/gaussian.jpg", im_gauss)
