
# برای چک کردن کد ، در عکس کراپ شده با لیبل های جدید دور گلبول های سفید یک کادر رسم میکنیم
import numpy as np
import cv2
import os
def show(path1: str,path2: str):
    im = cv2.imread(path1)
    with open(path2) as f:
        content = f.read()
    spl = content.split()
    le = len(spl)
    rows, cols = (int(le / 5), 5)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for j in range(0, le):
        arr[int((j) / 5)][j % 5] = spl[j]
    xs=[]
    ys=[]
    xe=[]
    ye=[]
    start_point=[]
    end_point=[]
    for i in range(0,int(le/5)):
        xs.append(int((im.shape[1]*float(arr[i][1]))-im.shape[1]*float(arr[i][3])/2))
        ys.append(int(im.shape[0]*float(arr[i][2])-im.shape[0]*float(arr[i][4])/2))
        start_point.append((xs[i],ys[i]))
        xe.append(int((im.shape[1]*float(arr[i][1]))+im.shape[1]*float(arr[i][3])/2))
        ye.append(int(im.shape[0]*float(arr[i][2])+im.shape[0]*float(arr[i][4])/2))
        end_point.append((xe[i],ye[i]))
        color = (0, 0, 255)
        thickness = 10
        image= cv2.rectangle(im, start_point[i], end_point[i], color, thickness)
    cv2.imshow('window_name', image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()