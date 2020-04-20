import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from menu_emparejamiento import *
from save_file import *


def brief(detector,emparejador,opcion,nombre1,nombre2,norma):
    
    if opcion == 'd':
        img1= cv.imread('graf1.png',cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread('graf3.png',cv.IMREAD_GRAYSCALE) # trainImage
    
    if opcion == 'db':
        img1= cv.imread('box1.png',cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread('box2.png',cv.IMREAD_GRAYSCALE) # trainImage    
        
    if opcion == 'n':
        img1= cv.imread(nombre1,cv.IMREAD_GRAYSCALE)          # queryImage
        img2 = cv.imread(nombre2,cv.IMREAD_GRAYSCALE) # trainImages
    
    
    star = cv.xfeatures2d.StarDetector_create()
    
    # Initiate ORB detector
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    # find the keypoints and descriptors with ORB
    kpa = star.detect(img1,None)
    kp1, des1 = brief.compute(img1,kpa)
    
    kpb = star.detect(img2,None)
    kp2, des2 = brief.compute(img1,kpb)
    
    imgx = cv.drawKeypoints(img1, kp1, None, color=(0,255,255))
    imgy = cv.drawKeypoints(img2, kp2, None, color=(0,255,255))
    window_namex="Rasgos Caracteristicos imagen 1"
    window_namey="Rasgos Caracteristicos imagen 2"
    cv.namedWindow(window_namex)
    cv.namedWindow(window_namey)
    cv.resizeWindow(window_namex,500,400)
    cv.resizeWindow(window_namey,500,400)
    cv.imshow(window_namex,imgx)
    cv.imshow(window_namey,imgy)
    save(imgx,emparejador,detector,norma,tag1)
    save(imgy,emparejador,detector,norma,tag2)

    menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2,norma,detector)    


tag1="Det1"
tag2="Det2"

    
if __name__ == "__main__":
    brief(detector,emparejador)
