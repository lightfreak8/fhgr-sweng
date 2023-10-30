"""
image_processor.py

class ImageProcessor:


changes:
1.0     2023-10-29      created


public functions:
    __init()__(self):   constructor, if not successfull set to None


"""
import cv2
import numpy as np

from camera import Camera
from point import Point
from shape import Shape
from polygon import Polygon
from circle import Circle

class ImageProcessor:
    #class constructor
    def __init__(self):
            """
            Initialize an ImageProcessor object.

            This class is responsible for processing image frames using a list of detectors.

            """
            self._detectors = [
                PatternDetector(),  # PatternDetector must come first, else no patterns for color detector
                ColorDetector(),
            ]
            self._pattern_color_list = []
            
    def detect(self, frame):
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
                patterns.append(pattern)
            else:
                center = Point()
                for p in points:
                    center.x += p.x
                    center.y += p.y
                center.x /= len(points)
                center.y /= len(points)
                radius = 0
                for p in points:
                    radius += np.sqrt((center.x - p.x)**2 + (center.y - p.y)**2)
                radius /= len(points)
                pattern = Circle(center, radius)
                patterns.append(pattern)

        return patterns

