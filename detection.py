import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import streamlit as st
import streamlit.components.v1 as components

def detect_objects(img_path):
    im= cv2.imread(img_path)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()

def detect_faces(img_path):
    im= cv2.imread(img_path)

    faces, confidences = cv.detect_face(im)

    for face in faces:
        (startX, startY) = face[0],face[1]
        (endX, endY) = face[2],face[3]
        cv2.rectangle(im,(startX,startY),(endX,endY),(0,255,0),2)

    plt.imshow(im)
    plt.show()

file = st.file_uploader(label="Загрузите фотографию")
detected = st.radio("Выберите, что нужно детектировать",("Детекция лиц","Детекция объектов"))


if(detected=="Детекция лиц"):
    detect_faces(file.name)
elif(detected=="Детекция объектов"):
    detect_objects(file.name)




