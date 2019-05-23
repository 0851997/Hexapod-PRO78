# USAGE
# python yolo_detector.py --yolo yolo-coco

import numpy as np
import argparse
import imutils
from imutils.video import VideoStream
import time
import cv2
import os

# Parameters to run this program
ap = argparse.ArgumentParser()
ap.add_argument("-y", "--yolo", required=True,
	help="base path to YOLO directory")
ap.add_argument("-c", "--confidence", type=float, default=0.8, #0.5
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3, #0.3
	help="threshold when applyong non-maxima suppression")
args = vars(ap.parse_args())

labelsPath = os.path.sep.join([args["yolo"], "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")

weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])

print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

vs = VideoStream(src=0).start()
time.sleep(1.0)
(W, H) = (None, None)

while True:
	frame = vs.read()
	if W is None or H is None:
		(H, W) = frame.shape[:2]
		print("[INFO] Height:", H, "Width:", W)

	# Making a blob and putting it through the layers of the yolo detection
	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	start = time.time()
	layerOutputs = net.forward(ln)
	end = time.time()

	boxes = []
	confidences = []
	classIDs = []

	for output in layerOutputs:
		for detection in output:
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			if LABELS[classID] in 'person': # Filter out off all the detected things to only persons
				if confidence > args["confidence"]:
					box = detection[0:4] * np.array([W, H, W, H])
					(centerX, centerY, width, height) = box.astype("int")

					x = int(centerX - (width / 2))
					y = int(centerY - (height / 2))

					boxes.append([x, y, int(width), int(height)])
					confidences.append(float(confidence))
					classIDs.append(classID)

	idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
		args["threshold"])

	if len(idxs) > 0: # If there is more than 0 persons detected draw it on the screen
		for i in idxs.flatten():
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])

			color = [int(c) for c in COLORS[classIDs[i]]]
			cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
			dimensionsRectangle = (((x+w)-x), ((y+h)-y))
			rectCenter = (int((x+x+w)/2), int((y+y+h)/2))
			distanceCenterToBorder = (dimensionsRectangle[0]/2, dimensionsRectangle[1]/2)
			cv2.circle(frame, rectCenter, 5, (0, 0, 210), 5)
			print("")
			print("[INFO] Width and Height of the found person   			:", dimensionsRectangle) 		#<---- dimensionsRectangle is the width and height of the box around the person
			print("[INFO] Center coordinates of the found person 			:", rectCenter) 				#<---- rectCenter is the center point of the found person
			print("[INFO] From the center to the border of the rectangle 	:", distanceCenterToBorder) 	#<---- distanceCenterToBorder is the distance between the found person center and the drawn border around it
			print("")
			text = "{}: {:.4f}".format(LABELS[classIDs[i]],
				confidences[i])
			cv2.putText(frame, text, (x, y - 5),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

	cv2.imshow("Little Heavy Mathametics", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
cv2.destroyAllWindows()
vs.stop()
