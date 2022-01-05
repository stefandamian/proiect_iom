# TechVidvan Vehicle counting and Classification

# Import necessary packages

import cv2
import csv
import collections
import numpy as np
from PyQt5 import QtGui
from src.tracker import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Initialize Tracker
tracker = EuclideanDistTracker()

# Initialize the videocapture object
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


def from_static_video(video, output_img, detection_info, img_graph, root, q):
    cap = cv2.VideoCapture(video)

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

        # set results
        detection_info[0].setText(str(up_list[0] + down_list[0]))
        detection_info[1].setText(str(up_list[1] + down_list[1]))
        detection_info[2].setText(str(up_list[2] + down_list[2]))
        detection_info[3].setText(str(up_list[3] + down_list[3]))
        detection_info[4].setText(str(up_list[4] + down_list[4]))
        detection_info[5].setText(str(up_list[5] + down_list[5]))
        detection_info[6].setText(str(sum(up_list) + sum(down_list)))

        # set img
        output_img.setPixmap(convert_cv_qt(img))

        # set graph
        types = ['Pers...', 'Bici...', 'Mași...', 'Moto...', 'Auto...', 'Cami...']
        numbers = [
            up_list[0] + down_list[0],
            up_list[1] + down_list[1],
            up_list[2] + down_list[2],
            up_list[3] + down_list[3],
            up_list[4] + down_list[4],
            up_list[5] + down_list[5],
        ]

        img_graph[0].clear()
        img_graph[0].bar(types, numbers, color=['#950952', '#FFD9DA', '#FC440F', '#F1D302', '#197BBD', '#0892A5'])
        img_graph[1].draw()

        q.put(numbers)

        if root.ui.stackedWidget.currentWidget() != root.ui.aux_page:
            break

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
    detection_info[6].setText(str(sum(frequency.values())))

    # set img
    output_img.setPixmap(convert_cv_qt(img))

    # set graph
    types = ['Pers...', 'Bici...', 'Mași...', 'Moto...', 'Auto...', 'Cami...']
    numbers = [frequency['person'], frequency['bicycle'], frequency['car'], frequency['motorbike'], frequency['bus'],
               frequency['truck']]

    img_graph[0].clear()
    img_graph[0].bar(types, numbers, color=['#950952', '#FFD9DA', '#FC440F', '#F1D302', '#197BBD', '#0892A5'])
    img_graph[1].draw()

    return numbers
