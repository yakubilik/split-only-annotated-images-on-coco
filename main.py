import json
import re
import glob, os
import cv2


json = open("cocoJsonName.json","r")
line = json.readline()

res = [i.start() for i in re.finditer("path", line)]

img_names = []
os.chdir("Path of the all images on coco")


for i in res:
    path = " "
    while(line[i]!=","):
        path = path+line[i]
        i=i+1
    split = path.split(" ")
    split2 = split[2].split("/")
    split2[3] = split2[3][:-1]
    img_names.append(split2[3])

sayac = 0
for file in glob.glob("*.jpeg"):
    if file in img_names:
        img = cv2.imread(file)
        cv2.imwrite("Path to save annotated images" + file, img)
        print(file)

