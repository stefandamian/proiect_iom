# TechVidvan Vehicle counting and Classification

# Import necessary packages

import cv2
import csv
import collections
import numpy as np
from PyQt5 import QtGui
from matplotlib.backends.backend_template import FigureCanvas

from src.tracker import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt

# Initialize Tracker
tracker = EuclideanDistTracker()

# Initialize the videocapture object
cap = cv2.VideoCapture('../testare/video-compress.mp4')
input_size = 320

# Detection confidence threshold
confThreshold = 0.2
nmsThreshold = 0.2

font_color = (0, 0, 255)
font_size = 0.5
font_thickness = 2

# Middle cross line position
middle_line_position = 225
up_line_position = middle_line_position - 15
down_line_position = middle_line_position + 15

# Store Coco Names in a list
classesFile = "resources/yolo/coco.names"
classNames = open(classesFile).read().strip().split('\n')

# class index for our required detection classes
required_class_index = [0, 1, 2, 3, 5, 7]

# detected_classNames = []

## Model Files
modelConfiguration = 'resources/yolo/yolov3-320.cfg'
modelWeigheights = 'resources/yolo/yolov3-320.weights'

# configure the network model
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigheights)

# Configure the network backend

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Define random colour for each class
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classNames), 3), dtype='uint8')


# Function for finding the center of a rectangle
def find_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


# List for store vehicle count information
temp_up_list = []
temp_down_list = []
up_list = [0, 0, 0, 0, 0, 0]
down_list = [0, 0, 0, 0, 0, 0]


# Function for count vehicle
def count_vehicle(box_id, img):
    x, y, w, h, id, index = box_id

    # Find the center of the rectangle for detection
    center = find_center(x, y, w, h)
    ix, iy = center

    # Find the current position of the vehicle
    if (iy > up_line_position) and (iy < middle_line_position):

        if id not in temp_up_list:
            temp_up_list.append(id)

    elif iy < down_line_position and iy > middle_line_position:
        if id not in temp_down_list:
            temp_down_list.append(id)

    elif iy < up_line_position:
        if id in temp_down_list:
            temp_down_list.remove(id)
            up_list[index] = up_list[index] + 1

    elif iy > down_line_position:
        if id in temp_up_list:
            temp_up_list.remove(id)
            down_list[index] = down_list[index] + 1

    # Draw circle in the middle of the rectangle
    cv2.circle(img, center, 2, (0, 0, 255), -1)  # end here
    # print(up_list, down_list)


# Function for finding the detected objects from the network output
def postProcess(outputs, img):
    detected_classNames = []
    height, width = img.shape[:2]
    boxes = []
    classIds = []
    confidenceScores = []
    detection = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if classId in required_class_index:
                if confidence > confThreshold:
                    w, h = int(det[2] * width), int(det[3] * height)
                    x, y = int((det[0] * width) - w / 2), int((det[1] * height) - h / 2)
                    boxes.append([x, y, w, h])
                    classIds.append(classId)
                    confidenceScores.append(float(confidence))

    # Apply Non-Max Suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidenceScores, confThreshold, nmsThreshold)
    # print(classIds)
    for i in indices.flatten():
        x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]
        # print(x,y,w,h)

        color = [int(c) for c in colors[classIds[i]]]
        name = classNames[classIds[i]]
        detected_classNames.append(name)
        # Draw classname and confidence score
        cv2.putText(img, f'{name.upper()} {int(confidenceScores[i] * 100)}%',
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        # Draw bounding rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
        detection.append([x, y, w, h, required_class_index.index(classIds[i])])

    # Update the tracker for each object
    boxes_ids = tracker.update(detection)
    for box_id in boxes_ids:
        count_vehicle(box_id, img)

    return detected_classNames


def convert_cv_qt(cv_img):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
    return QPixmap.fromImage(p)


def realTime():
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
        ih, iw, channels = img.shape
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False)

        # Set the input of the network
        net.setInput(blob)
        layersNames = net.getLayerNames()
        outputNames = [(layersNames[i - 1]) for i in net.getUnconnectedOutLayers()]
        # Feed data to the network
        outputs = net.forward(outputNames)

        # Find the objects from the network output
        postProcess(outputs, img)

        # Draw the crossing lines
        cv2.line(img, (0, middle_line_position), (iw, middle_line_position), (255, 0, 255), 2)
        cv2.line(img, (0, up_line_position), (iw, up_line_position), (0, 0, 255), 2)
        cv2.line(img, (0, down_line_position), (iw, down_line_position), (0, 0, 255), 2)

        # Draw counting texts in the frame
        cv2.putText(img, "Up", (110, 20), cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Down", (160, 20), cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Person:        " + str(up_list[0]) + "     " + str(down_list[0]), (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Bycicle:        " + str(up_list[1]) + "     " + str(down_list[1]), (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Car:        " + str(up_list[2]) + "     " + str(down_list[2]), (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Motorbike:  " + str(up_list[3]) + "     " + str(down_list[3]), (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Bus:        " + str(up_list[4]) + "     " + str(down_list[4]), (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)
        cv2.putText(img, "Truck:      " + str(up_list[5]) + "     " + str(down_list[5]), (20, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, font_thickness)

        # Show the frames
        cv2.imshow('Output', img)

        if cv2.waitKey(1) == ord('q'):
            break

    # Write the vehicle counting information in a file and save it

    with open("../testare/test/data.csv", 'w') as f1:
        cwriter = csv.writer(f1)
        cwriter.writerow(['Direction', 'car', 'motorbike', 'bus', 'truck'])
        up_list.insert(0, "Up")
        down_list.insert(0, "Down")
        cwriter.writerow(up_list)
        cwriter.writerow(down_list)
    f1.close()
    # print("Data saved at 'data.csv'")
    # Finally realese the capture object and destroy all active windows
    cap.release()
    cv2.destroyAllWindows()


def from_static_image(image, output_img, detection_info, img_graph):
    img = cv2.imread(image)

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False)

    # Set the input of the network
    net.setInput(blob)
    layersNames = net.getLayerNames()
    outputNames = [(layersNames[i - 1]) for i in net.getUnconnectedOutLayers()]
    # Feed data to the network
    outputs = net.forward(outputNames)

    # Find the objects from the network output
    detected_classNames = postProcess(outputs, img)
    # count the frequency of detected classes
    frequency = collections.Counter(detected_classNames)

    # set results
    detection_info[0].setText(str(frequency['person']))
    detection_info[1].setText(str(frequency['bicycle']))
    detection_info[2].setText(str(frequency['car']))
    detection_info[3].setText(str(frequency['motorbike']))
    detection_info[4].setText(str(frequency['bus']))
    detection_info[5].setText(str(frequency['truck']))

    # set img
    output_img.setPixmap(convert_cv_qt(img))

    # set graph
    fig = plt.figure()
    types = ['Persoane', 'Biciclete', 'Mașini', 'Motociclete', 'Autobuze', 'Camioane']
    numbers = [frequency['person'], frequency['bicycle'], frequency['car'], frequency['motorbike'], frequency['bus'], frequency['truck']]
    plt.bar(types, numbers)

    img_graph[0].axes.plot([0,1,2,3,4], [10,1,20,3,40])
    img_graph[1] = img_graph[0]
