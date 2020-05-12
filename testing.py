import cv2 as cv
import numpy as np

blank_image = np.zeros(shape=[64, 64, 3], dtype=np.uint8)
ret, bw_img = cv.threshold(blank_image, 127,255, cv.THRESH_BINARY)
print(bw_img[0][0])
for i in range(0,64):
    for j in range(0,64):
        if j % 2 == 0:
            bw_img[i][j] = 255

cv.imshow("Black Blank", bw_img)

# img = cv.imread('input/testImage.jpg')
# # import cv2
# # image = cv2.imread("sample.jpg")
# newimg = cv.resize(img,(1024, 1024))
# # cv.imshow('image', newimg)
# # cv.waitKey(0)
# cv.destroyAllWindows()
# for i in range(0, 1024):
#     for j in range(0,1024):
#         newimg[i, j][0] = 0                                                              
#         # print(pixel[0])

# cv.imshow('image', newimg)
cv.waitKey(0)
cv.destroyAllWindows()
