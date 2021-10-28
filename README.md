# split-only-annotated-images-on-coco

This code written for splitting only annotated images on coco.

When you are annotating images on coco, there might be some images that you didn't annotate. 
When you export the annotations i didn't see any way to collect only the annotated images. So i had to do it manually.

All this code does, reads the ".json" file that coco gives, then splits it by image paths and collects the annotated image names. Then from directory of all images, reads only annotated images and saves them some other directory.
