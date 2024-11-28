#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import copy
import time
import cv2 as cv
from annotate import xml_builder
import os

project_path = os.getcwd()
myxml_builder = xml_builder(project_path)


status = "new" #new/update
model_name = 'pills'
label_class_name = 'uncomplete_pill'

def isint(s):
    p = '[-+]?\d+'
    return True if re.fullmatch(p, s) else False


def initialize_tracker(window_name, image):
    params = cv.TrackerDaSiamRPN_Params()
    params.model = "model/dasiamrpn_model.onnx"
    params.kernel_r1 = "model/dasiamrpn_kernel_r1.onnx"
    params.kernel_cls1 = "model/dasiamrpn_kernel_cls1.onnx"
    tracker = cv.TrackerDaSiamRPN_create(params)
    tracker2 = cv.TrackerDaSiamRPN_create(params)
    
    while True:
        bbox = cv.selectROI(window_name, image)
        bbox2 = cv.selectROI(window_name, image)

        try:
            tracker.init(image, bbox)
            tracker2.init(image, bbox2)
        except Exception as e:
            print(e)
            continue

        return (tracker, tracker2)



def main():
    color_list = [
        [20, 100, 250],  
        [200, 10, 20],  
    ]

    

    #############################################################
    window_name = 'Annotation'
    cv.namedWindow(window_name)

    

    rootdir = f"{project_path}/data/{model_name}/JPEGImages"
    image = cv.imread(f'{rootdir}/1.png')
    h, w, c = image.shape
    tracker, tracker2 = initialize_tracker(window_name, image )
    frame_number = 1
    count = 1
    img_list = []
    image_list = []
    directory = rootdir
    # Use a single loop to fetch images in sequence
    for i in range(1, len(os.listdir(rootdir))+1):
        filename = f"{i}.png"
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            image_list.append(file_path)
        else:
            print(f"File {filename} does not exist.")

    # Print the list of images
    print("Image files in sequence:")
    for image in image_list:
        print(image)
    
    for x in image_list:
        image = cv.imread(x)
        debug_image = copy.deepcopy(image)
        start_time = time.time()
        ok, bbox = tracker.update(image)
        ok, bbox2 = tracker2.update(image)
        elapsed_time = time.time() - start_time
        if ok:
            xmin = bbox[0]
            ymin = bbox[1]
            xmax = bbox[2]
            ymax = bbox[3]
            image_path = f"{project_path}/data/{model_name}/JPEGImages/file{frame_number}.png"
            xml_path = f"{project_path}/data/{model_name}/Annotations/file{frame_number}.xml"
            cv.imwrite(image_path ,image)
            if status == 'new':
                myxml_builder.build_xml_file(image_path,xml_path, w, h, xmin, ymin, xmax, ymax, label_class_name)
            elif status == 'update':
                myxml_builder.update_xml_file(image_path,xml_path, w, h, xmin, ymin, xmax, ymax, label_class_name)
            cv.rectangle(debug_image, bbox, color_list[0], thickness=1)
            cv.putText(debug_image,'Model' + " : " + '{:.1f}'.format(elapsed_time * 1000) + "ms",(10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, color_list[0], 2,cv.LINE_AA)

            cv.rectangle(debug_image, bbox2, color_list[1], thickness=1)
            cv.putText(debug_image,'Model' + " : " + '{:.1f}'.format(elapsed_time * 1000) + "ms",(10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, color_list[0], 2,cv.LINE_AA)
        
        cv.imshow(window_name, debug_image)
        frame_number = frame_number + 1

        k = cv.waitKey(1)
        if k == 32:  # SPACE
            tracker, tracker2 = initialize_tracker(window_name, image)
        if k == 27:  # ESC
            break


if __name__ == '__main__':
    main()