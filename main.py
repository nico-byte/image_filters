import cv2
import low_pass, gaussian, sobel, laplace, median


low_pass
gaussian
sobel
laplace
median

cv2.namedWindow("low-pass filtered", cv2.WINDOW_NORMAL)
cv2.resizeWindow("low-pass filtered", 350, 250)
cv2.moveWindow("low-pass filtered", 100, -100)
im_low_pass = cv2.imread("examples/low_pass.jpg", 1)
cv2.imshow("low-pass filtered", im_low_pass)

cv2.namedWindow("gaussian filtered", cv2.WINDOW_NORMAL)
cv2.resizeWindow("gaussian filtered", 350, 250)
cv2.moveWindow("gaussian filtered", 450, -100)
im_gaussian = cv2.imread("examples/gaussian.jpg", 1)
cv2.imshow("gaussian filtered", im_gaussian)

cv2.namedWindow("sobel filtered", cv2.WINDOW_NORMAL)
cv2.resizeWindow("sobel filtered", 350, 250)
cv2.moveWindow("sobel filtered", 100, 500)
im_sobel = cv2.imread("examples/sobel.jpg", 1)
cv2.imshow("sobel filtered", im_sobel)

cv2.namedWindow("laplace filtered", cv2.WINDOW_NORMAL)
cv2.resizeWindow("laplace filtered", 500, 500)
cv2.moveWindow("laplace filtered", 900, 250)
im_laplace = cv2.imread("examples/laplace.jpg", 1)
cv2.imshow("laplace filtered", im_laplace)

cv2.namedWindow("median filtered", cv2.WINDOW_NORMAL)
cv2.resizeWindow("median filtered", 350, 250)
cv2.moveWindow("median filtered", 450, 500)
im_median = cv2.imread("examples/median.jpg", 1)
cv2.imshow("median filtered", im_median)

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
