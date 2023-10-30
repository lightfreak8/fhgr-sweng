from polygon import Polygon
from circle import Circle

import cv2

class Display:
    def __init__(self, name):
        self.name = name
        self.frame = None

    def drawContours(self, frame, shapes):
        contour_color = (0, 255, 0)
        for shape in shapes:
            x = None
            y = None
            if isinstance(shape, Polygon):
                contour = shape.getContour()
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(frame, [contour], -1, contour_color, 2)

            elif isinstance(shape, Circle):
                x = int(round(shape.origin.x))
                y = int(round(shape.origin.y))
                cv2.circle(frame, [x, y], int(round(shape.radius)), contour_color, 2)

            else:
                raise Exception(f'Unknown shape encountered ({type(shape)})')

            cv2.putText(frame, shape.color + " " + shape.getName(), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120, 120, 255), 2)
        cv2.imshow(self.name, frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



