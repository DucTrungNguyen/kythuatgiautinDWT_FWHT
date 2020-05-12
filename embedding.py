# from PIL import Image
import pywt
import pywt.data
from sympy import fwht, ifwht
from mpmath import mp
import math
import numpy as np
import cv2 as cv
import helper as h
import os
def embedding(pathhostimge, pathwatermarkimage):


    # Kiem tra xem file co ton tai hay khong
    if not os.path.exists(pathhostimge) or not os.path.exists(pathwatermarkimage):
        print("STOPPPPP: Image not exists")
        exit()

    #Doc anh thuy van va dua ve dang nhi phan va resize ve kich co 64x64
    image_watermark = cv.imread(pathwatermarkimage, 2)
    ret, bw_img = cv.threshold(image_watermark, 127,255, cv.THRESH_BINARY)
    new_image_watermark = cv.resize(bw_img, (64, 64))
    cv.imwrite('output/watermarkResulted.png', new_image_watermark) 
    dataWater = []
    for i in range(0, 64):
        for j in range(0, 64):
            # print(new_image_watermark[i][j])
            dataWater.append(new_image_watermark[i][j])


    # Doc anh host, resize ve kich co 1024x1024 va tach kenh mau R
    img = cv.imread(pathhostimge)
    new_imageHost = cv.resize(img, (1024, 1024))

    r1 = []

    x = []

    for i in range(0, 1024):
        x = [new_imageHost[i, j][0] for j in range(0,1024)]
        r1.append(x)
        x = []

    # Thuc hien DWT 2 chieu 2 lan dua kenh mau ve kich co 256x256
    coeffs1 = pywt.dwt2(r1, wavelet= 'db1')
    LL1, (LH1, HL1, HH1) = coeffs1
    coeffs2 = pywt.dwt2(HH1, wavelet='db1')
    LL2, (LH2, HL2, HH2) = coeffs2
   

    # Thuc hien FWHT
    fwhtHH2 = fwht(HH2)

    # Chia thanh cac khoi co kich co 4x4. Tong so khoi la 64x64
    blocks = h.divblock(fwhtHH2)

    #Thuc hien Embeding giua kenh mau R va anh Thuy van
    newBlocks = hessenberg(blocks=blocks, dataWater=dataWater)

    #Gop cac khoi lai voi nhau
    combinedblocks = h.combinblocks(newBlocks)

    # Thuc hien Inverse FWHT
    ifwhtHHw = ifwht(np.array(combinedblocks))


    # Thuc hien Inverse  DWT 2 chieu 2 lan, dua ve kich co 1024x1024
    coeffs3 = (LL2, (LH2, HL2, ifwhtHHw))
    X = pywt.idwt2(coeffs3, wavelet='db1')

    coeffs4 = (LL1, (LH1, HL1, X))
    Rcomma = pywt.idwt2(coeffs4, wavelet='db1')

    #Gan kenh mau R moi vao anh cu va hien anh da duoc thuy van
    for i in range(0, 1024):
        for j in range(0, 1024):
            new_imageHost[i][j][0] = abs(round(float(Rcomma[i][j])))
    cv.imwrite('output/ImageResulted.png', new_imageHost)
    cv.imshow("WaterMarked", new_imageHost)
    cv.waitKey(0)
    cv.destroyAllWindows()


def hessenberg(blocks, dataWater):
    step = 0.034
    pixelWater = 64*64

    for h in range(0, pixelWater):
        block = mp.matrix(blocks[h])
        Q, H = mp.hessenberg(block)
        h11 = H[0, 0]
        if dataWater[h] == 255:
            M1 = 0.5*step
            M2 = -1.5*step
        elif dataWater[h] == 0:
            M1 = -0.5*step
            M2 = 1.5*step

        h11 = H[0, 0]
        k = math.floor((math.ceil(h11 / step)) / 2)
        T1 = 2*k*step + M1
        T2 = 2*k*step + M2
        if abs(h11 - T2) < abs(h11 - T1):
            h11new = T2
        else:
            h11new = T1
        newH = []
        newQ = []
        for i in range(0, 4):
            rowH = []
            rowQ = []
            for j in range(0, 4):
                x = round(H[i, j])
                rowH.append(x)
                x = Q[i, j]
                rowQ.append(x)
            newH.append(rowH)
            newQ.append(rowQ)
        newblock = np.dot(np.dot(np.array(newQ), np.array(newH)), np.array(newQ).T).tolist()
        blocks[h] = newblock
    print("=========")
    print(blocks[0])
    return blocks
