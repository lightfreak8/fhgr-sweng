"""
added code for testing class camera.py

"""


# import class
from camera import Camera
from point import Point
from shape import Shape
from polygon import Polygon
from circle import Circle
from image_processor import ImageProcessor

def test_point():
    point = Point(2, 4)
    print(point)
    point.x = 4.3
    point.y = 2.8
    print(point)

def test_polygon():
    print("=== Polygon Test ===")
    try:
        polygon = Polygon([1, 2])
    except Exception as ex:
        print(ex)
    try:
        polygon = Polygon([1, 2, 4])
    except Exception as ex:
        print(ex)
    poly = Polygon([Point(1, 2), Point(3, 4), Point(5, 6)])
    print(f'Polygon Points: {poly} ({poly.getName()})')
    poly = Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8)])
    print(f'Polygon Points: {poly} ({poly.getName()})')
    poly = Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10)])
    print(f'Polygon Points: {poly} ({poly.getName()})')
    poly = Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10), Point(11, 12)])
    print(f'Polygon Points: {poly} ({poly.getName()})')
    poly = Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10), Point(11, 12), Point(13, 14)])
    print(f'Polygon Points: {poly} ({poly.getName()})')

def test_circle():
    print('=== Circle Test ===')
    try: circle = Circle(1, 2)
    except Exception as ex: print(ex)
    circle = Circle(Point(1, 2), 3)
    print(f'Circle: {circle} ({circle.getName()})')

def test_shape():
    print('=== Shape Test ===')
    shapes = [Circle(Point(1, 2), 3),
              Polygon([Point(1, 2), Point(3, 4), Point(5, 6)]),
              Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10), Point(11, 12)]),
              Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10)]),
              Circle(Point(8, 9), 10.2),
              Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10)]),
              Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8)]),
              Polygon([Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10), Point(11, 12), Point(13, 14)])
             ]
    for i in range(len(shapes)):
        print(f'[{i}] : {shapes[i].getName()} -> {shapes[i]}')

def main():
    # testing point class
    #test_point()

    # testing polygon class
   # test_polygon()

    # testing circle class
    #test_circle()

    # testing shapes together
   # test_shape()

    #testing camera class
    camera = Camera()
    # img = camera.requestImage()
    # camera.showImage(img)
    path = "../find-shapes/data/sample_image.jpg"
    sample = camera.requestSample(path)
    camera.showImage(sample)
    
    detect = ImageProcessor()
    shapes = detect.detect(sample)
    for i in range(len(shapes)):
        print(f'[{i}] : {shapes[i].getName()} -> {shapes[i]}')

    camera.release()

if __name__ == "__main__":
    main()

