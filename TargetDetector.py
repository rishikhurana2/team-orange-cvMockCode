import cv2
import numpy as np

class TargetDetector:
	def __init__(self):
		self.threshed = None
		self.approx = None
		self.contr = None
		self.HSV = None
	def threshold(self, originalImage):
		self.HSV = cv2.cvtColor(originialImage, cv2.COLOR_BGR2HSV)
		THRESHOLD_MIN = np.array([0,0,0], np.uint8)
		THRESHOLD_MAX = np.array([255,100,100]. np.uint8)
		self.threshed = cv2.inRange(self.HSV, THRESHOLD_MIN, THRESHOLD_MAX)
		cv2.imshow("Threshed Image", self.threshed)
	def contour(self, threshedImg, originalImg):
		count = -1
		images, contours, hierarchy = cv2.findContours(threshedImg, cv2.RETR, cv2.CHAIN_APPROX_SIMPLE)
		for cont in contour:
			count = count + 1
			self.approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont, True), True)
			area = cv2.contourArea(approx)
			if (len(self.approx) >= 4 and area > 500):
				cv2.drawContours(originalImg, contours, count, (255,10,255), 5)
		cv2.imshow("Contoured Image", originalImg)
		self.contr = originalImg
	def getApprox(self):
		return self.approx
	def getContour(self):
		return self.contr
	def getHSV(self):
		return self.HSV
	def getThreshed(self):
		return self.threshed