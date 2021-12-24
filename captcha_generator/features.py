import cv2
import numpy as np
from statistics import mode

net = cv2.dnn.readNetFromDarknet("yolo/yolov3.cfg", "yolo/yolov3.weights") #608
classes = []
class_ids = []
confidences = []
boxes = []

def detectAndFill(path):
    with open('yolo/coco.names', 'r') as f:
        classes = f.read().strip().split('\n')
    output_layers = [net.getLayerNames()[i-1] for i in net.getUnconnectedOutLayers()]

    image = cv2.imread(path)
    height, width = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1/255, (608,608), (0,0,0), True, crop = False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    for out in outs:
        for detection in out:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                X = int(center_x - w / 2)
                Y = int(center_y - h / 2)

                boxes.append([X,Y,w,h])
                confidences.append(round(confidence, 3))
                class_ids.append(classID)
    temp_lst = []
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in range(len(boxes)):
        if i in indexes:
            label = classes[class_ids[i]]
            temp_lst.append(label)
    for i in range(len(boxes)):
        if i in indexes:
            label = classes[class_ids[i]]
            if label == mode(temp_lst):
                x,y,w,h = boxes[i]
                cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), cv2.FILLED)
    cv2.imwrite('input_image/object_detect/detect.png', image)

def chop(path):
    image = cv2.imread(path)
    H,W = image.shape[:2]
    x = W // 3 # x increment
    y = H // 3 # y increment
    count = 0
    for i in range(1,4):
        for j in range(1,4):
            output = image[(i-1)*y:i*y, (j-1)*x:j*x]
            cv2.imwrite(f'input_image/chopped_up/{count}.png', output)
            count += 1

def squareify(path):
    image = cv2.imread(path)
    H,W = image.shape[:2]
    side = min(H, W)
    output = image[(H-side)//2:H-(H-side)//2, (W-side)//2:W-(W-side)//2]
    cv2.imwrite('input_image/squareified/squareImage.png', output)

def greenCount(path):
    image = cv2.imread(path)
    amount = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            b, g, r = image[x, y]
            if (b, g, r) == (0,255,0):
                amount += 1
    return amount

def checkGreen():
    green_count = []
    output = []
    for x in range(9):
        num = greenCount(f'input_image/chopped_up/{x}.png')
        green_count.append(num)
    standard = max(green_count)
    for x in green_count:
        if x > standard * 0.2:
            output.append(True)
        else:
            output.append(False)
    return output
