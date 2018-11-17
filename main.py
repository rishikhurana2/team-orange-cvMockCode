from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from Target import Target
import cv2

cameraID = 0

cam = cv2.VideoCapture(cameraID)
detector = TargetDetector()
target = Target()
processor = TargetProcessor()

while(True):
	ret,frame = cam.read()
	if not ret:
		continue
	detector.threshold(frame)
	detector.contour(detector.getThreshed(), frame)
	width = target.getWidth()
	height = target.getHeight()
	centerX, centerY = target.getCenter()
	shape = target.getShape()
	processor.calculate(width, height, centerX, centerY, detector.getHSV(), shape)
	azi = processor.getAzi()
	alti = processor.getAlti()
	dist = processor.getDist()
	print("Azimuth: " + str(azi))
	print("Altitude: " + str(alti))
	print("Distance: " + str(dist))
	if (cv2.waitKey(10) == 27):
		break