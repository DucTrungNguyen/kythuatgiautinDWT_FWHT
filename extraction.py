import pywt
import pywt.data
from sympy import fwht, ifwht
from mpmath import mp
import math
import numpy as np
import cv2 as cv
import helper as h
import os


def extraction():
    # Kiem tra xem file co ton tai hay khong
    if not os.path.exists('output/watermarkResulted.png') or not os.path.exists('output/ImageResulted.png'):
        print("STOPPPPP: Image not exists")
        exit()

    # Doc anh thuy phan
    image_watermark = cv.imread('output/watermarkResulted.png', 2)
    # print(image_watermark[0][0])
    dataWater = []
    for i in range(0, 64):
        for j in range(0, 64):
            dataWater.append(image_watermark[i][j])

    # Tao 1 anh trang de dung trong qua trinh trich xuat
    blank_image = np.zeros(shape=[64, 64, 3], dtype=np.uint8)
    ret, imgExtrac = cv.threshold(blank_image, 127, 255, cv.THRESH_BINARY)

    # Doc anh host da duoc thuy van
    img = cv.imread('output/ImageResulted.png')
    r1 = []
    x = []
    for i in range(0, 1024):
        x = [img[i][j][0] for j in range(0, 1024)]
        r1.append(x)
        x = []

    #Thuc hien bien doi DWT 2 chieu 2 lan dua ve kich vo 256x256
    coeffs1 = pywt.dwt2(r1, wavelet= 'db1')
    LL1, (LH1, HL1, HH1) = coeffs1
    coeffs2 = pywt.dwt2(HH1, wavelet='db1')
    LL2, (LH2, HL2, HH2) = coeffs2

    #Thuc hien bien doi FWHT
    fwhtHH2 = fwht(HH2)

    #Chia thanh cac khoi 4x4. Tong cos 64x64 khoi
    blocks = h.divblock(fwhtHH2)


    # dataWater = []
    step = 0.034
    #Thuc hien trich xuat anh thuy van va hien len
    for i in range(0, 64*64):

        block = mp.matrix(blocks[i])
        # print(block)
        Q , H = mp.hessenberg(block)

        h11 = H[0, 0]
        # print(h11)
        if math.ceil(h11/step) % 2 == 0:
            pixelExtrac = 0
        elif math.ceil(h11/step) % 2 == 1:
            pixelExtrac = 255

        dataWater.append(pixelExtrac)

    for i in range(0,64):
        for j in range(0, 64):
            imgExtrac[i][j] = dataWater[i * 64 + j]
    print('Have showed watermark')
    cv.imshow("Extraction Image", imgExtrac)
    cv.waitKey(0)
    cv.destroyAllWindows()
