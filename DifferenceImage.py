import cv2

img1 = cv2.imread('mobil1.jpg')
img1 = cv2.resize(img1, (600, 300))
img2 = cv2.imread('mobil2.jpg')
img2 = cv2.resize(img2, (600, 300))

diff_img = cv2.absdiff(img1, img2)

cv2.imshow('Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows