"""
display.py

class Display:
show images on the display

changes:
1.0     2023-10-27      created
1.1     2023-11-02      drawContours: clone the frame and then do stuff with it
1.1.1   2023-11-05      fix: function descriptions

"""


from polygon import Polygon
from circle import Circle

import cv2

KEY_ESC = 27

class Display:
    def __init__(self, name, ms_wait=30):
        """
        Constructor for the Display class
        Args:
            name, for the window
            ms_wait, wait time for cv2.waitKey(); 0 to require key press to continue
        """
        self.name = name
        self.frame = None
        self.ms_wait = ms_wait
        self.alive = True

    def __del__(self):
        """
        Destructor for the Display class
        """
        cv2.destroyAllWindows()

    def drawContours(self, frame, shapes):
        """
        Draw the contours from various shapes onto a frame
        Args:
            frame, the input image frame
            shapes, the input shapes
        """
        this_frame = frame.copy()
        contour_color = (0, 255, 0)
        for shape in shapes:
            x = None
            y = None
            if isinstance(shape, Polygon):
                contour = shape.getContour()
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(this_frame, [contour], -1, contour_color, 2)

            elif isinstance(shape, Circle):
                x = int(round(shape.origin.x))
                y = int(round(shape.origin.y))
                cv2.circle(this_frame, [x, y], int(round(shape.radius)), contour_color, 2)

            else:
                raise Exception(f'Unknown shape encountered ({type(shape)})')

            cv2.putText(this_frame, shape.getColor() + " " + shape.getName(), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120, 120, 255), 2)
        cv2.imshow(self.name, this_frame)
        key = cv2.waitKey(self.ms_wait)
        if key >= 0:
            if chr(key) in 'qQ' or key == KEY_ESC:
                self.alive = False
        #cv2.destroyAllWindows()



