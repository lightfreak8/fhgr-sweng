"""
image_processor.py

class ImageProcessor:
process images

changes:
1.0     2023-10-28      created
1.1     2023-10-29      added detect


public functions:
    __init__(self):     constructor, if not successfull set to None
    createTimestamp(self):  return timestamp
    detect(self, image): detect 


"""

import cv2
import numpy as np

from datetime import datetime

from camera import Camera
from point import Point
from shape import Shape
from polygon import Polygon
from circle import Circle

class ImageProcessor:
    #class constructor
    def __new__(self, frame = None):
        shapes = DetectShape(frame)
        return shapes
    
    def createTimestamp(self):
        dt = datetime.now()
        return dt

class DetectShape:
    def __new__(self, frame):
        return self.detectShape(self, frame)
    
    def detectShape(self, frame):
        """
        Detect patterns (shapes) in a given image frame.

        Args:
            patterns (list): A list to store detected Pattern objects.
            frame (numpy.ndarray): The input image frame.

        Returns:
            list: A list of Pattern objects representing the detected patterns.
        """
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Perform dilation
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 40, 180)
        # Perform dilation
        kernel = np.ones((5, 5), np.uint8)
        dilated_image = cv2.dilate(edges, kernel, iterations=2)
        # detect contours
        contours, _ = cv2.findContours(
            dilated_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        approx = None
        patterns = []
        for contour in contours:
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            points = []
            for p in approx:
                points.append(Point(p[0,0], p[0,1]))

            if len(points) < 6:
                pattern = Polygon(points)
                pattern.color = DetectColor(pattern, frame)
                patterns.append(pattern)
            else:
                center = Point()
                for p in points:
                    center.x += p.x
                    center.y += p.y
                center.x /= len(points)
                center.y /= len(points)
                center.x = int(round(center.x))
                center.y = int(round(center.y))
                radius = 0
                for p in points:
                    radius += np.sqrt((center.x - p.x)**2 + (center.y - p.y)**2)
                radius /= len(points)
                radius = int(round(radius))
                pattern = Circle(center, radius)
                pattern.color = DetectColor(pattern, frame)
                patterns.append(pattern)

        return patterns

class DetectColor:
    def __new__(self, shape, frame):
        return self.detectColor(self, shape, frame)
    
    def detectColor(self, shape, frame):
        """
        Detect color in shape

        Args:
            shape: ...

        Returns:
            color: string
        """
    
        mask = np.zeros_like(frame)
        if isinstance(shape, Polygon):
            cv2.drawContours(
                mask, [shape.getContour()], -1, (255, 255, 255), thickness=cv2.FILLED)
        elif isinstance(shape, Circle):
            cv2.circle(mask, [shape.origin.x, shape.origin.y], shape.radius,-1, (255, 255, 255), thickness=cv2.FILLED )

        masked_image = cv2.bitwise_and(frame, mask)
        # Convert the masked image to HSV color space
        hsv_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)

        # Get the hue channel from the HSV image
        hue_channel = hsv_image[:, :, 0]

        # Calculate the mean hue of non-zero values
        non_zero_hues = hue_channel[hue_channel != 0]
        median_hue = np.median(non_zero_hues)

        shape.color = self._hue_to_color(median_hue)
        


    def _hue_to_color(self, hue):
        """
        Convert a hue value to a color name.

        Args:
            hue (float): The hue value to be converted.

        Returns:
            str: The color name corresponding to the hue value.
        """
        color = ""
        if hue < 10:
            color = "RED"
        elif hue < 22:
            color = "ORANGE"
        elif hue < 33:
            color = "YELLOW"
        elif hue < 78:
            color = "GREEN"
        elif hue < 131:
            color = "BLUE"
        elif hue < 150:
            color = "VIOLET"
        else:
            color = "RED"
        return color

