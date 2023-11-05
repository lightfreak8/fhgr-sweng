"""
image_processor.py

class ImageProcessor:
Process images and create timestamp.

class DetectShape:
Detect patterns circle and different kind of polygons.

class DetectColor:
Detect median color in pattern.

changes:
1.0     2023-10-28      created
1.1     2023-10-29      added detect
1.2     2023-11-02      add 2 types of filtering: intersecting and points that are too close to other lines
1.2.1   2023-11-05      add comments / descriptions

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
    """
    public functions:
    __new__(self, frame):       constructor, if not successfull set to None
    createTimestamp(self):      return timestamp
    """
    def __new__(self, frame = None):
        """
        constructor, creating and returning a new instance
        Args:
            frame, the input image frame.
        Returns:
            shapes, list of patterns
            timestamp, string
        """
        shapes = DetectShape(frame)
        timestamp = self.createTimestamp(self)
        return (shapes, timestamp)

    def createTimestamp(self):
        dt = datetime.now()
        return dt

class DetectShape:
    """
    public functions:
    __new__(self, frame):       constructor, if not successfull set to None
    detect(self, image, mindist, allow_intersect)
    """

    def __new__(self, frame=None):
        """
        constructor
        Args:
            frame, the input image frame.
        Return
        """
        return self.detectShape(self, frame)

    def detectShape(self, frame, mindist=7, allow_intersect=False):
        """
        Detect patterns (shapes) in a given image frame.

        Args:
            frame, the input image frame.
        Returns:
            list: A list of Pattern objects representing the detected patterns.
        """
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Perform dilation
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        edges = cv2.Canny(blurred, 40, 180)
        # Perform dilation
        kernel = np.ones((3, 3), np.uint8)
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

            # filter out garbage - mindist
            #print(15*'=')
            garbage = False
            for i1 in range(len(points)):
                p1 = points[i1]
                for i2 in range(len(points)+1):
                    i21 = (i2+0) % len(points)
                    i22 = (i2+1) % len(points)
                    if i21 == i1 or i22 == i1: continue
                    p21 = points[i21]
                    p22 = points[i22]
                    dist = p1.dist(p21, p22)
                    #print(f'[{i1}] -> [{i21}, {i22}] : {dist}')
                    if dist < mindist:
                        #print('(garbage)')
                        garbage = True
                    if garbage: break
                if garbage: break

            # filter out garbage - intersection
            if not allow_intersect:
                for i1 in range(len(points)- 1):
                    i11 = i1+0
                    i12 = i1+1
                    p11 = points[i11]
                    p12 = points[i12]
                    for i2 in range(len(points)+1):
                        i21 = (i2+0) % len(points)
                        i22 = (i2+1) % len(points)
                        if i11 == i21 or i11 == i22 or i12 == i21 or i12 == i22: continue
                        p21 = points[i21]
                        p22 = points[i22]
                        #print(f'[{i1}, {i1+1}] x [{i2}, {i2+1}]')
                        if p11.is_intersect(p12, p21, p22):
                            garbage = True
                        if garbage: break
                    if garbage: break

            # ignore current if we want to filter out garbage
            if garbage:
                continue

            # valid points here
            if len(points) > 5:
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
            elif len(points) > 2:
                pattern = Polygon(points)
                pattern.color = DetectColor(pattern, frame)
                patterns.append(pattern)

        return patterns

class DetectColor:
    def __new__(self, shape, frame):
        """
        constructor
        Args:
            frame, the input image frame.
            shape (string), pattern
        Returns:
            color (string), median of colors in pattern
        
        """
        return self.detectColor(self, shape, frame)

    def detectColor(self, shape, frame):
        """
        Detect color in shape
        Args:
            shape (string), pattern
            frame, the input image frame.

        Returns:
            color (string), median of colors in pattern
        """

        mask = np.zeros_like(frame)
        if isinstance(shape, Polygon):
            cv2.drawContours(
                mask, [shape.getContour()], -1, (255, 255, 255), thickness=cv2.FILLED)
        elif isinstance(shape, Circle):
            cv2.circle(mask, [shape.origin.x, shape.origin.y], shape.radius, (255, 255, 255), thickness=cv2.FILLED )

        masked_image = cv2.bitwise_and(frame, mask)
        # Convert the masked image to HSV color space
        hsv_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)

        # Get the hue channel from the HSV image
        hue_channel = hsv_image[:, :, 0]

        # Calculate the mean hue of non-zero values
        non_zero_hues = hue_channel[hue_channel != 0]
        median_hue = np.median(non_zero_hues)

        return self._hue_to_color(self, median_hue)



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

