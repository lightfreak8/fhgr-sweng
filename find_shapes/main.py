"""
added code for testing class camera.py

"""


# import class
from camera import Camera
from point import Point
from shape import Shape

def test_point():
    point = Point(2, 4)
    print(point)
    point.x = 4.3
    point.y = 2.8
    print(point)

def main():
    # testing point class
    test_point()

    #testing camera class
    camera = Camera()
    img = camera.requestImage()
    camera.showImage(img)
    path = "../find-shapes/data/sample_image.jpg"
    sample = camera.requestSample(path)
    camera.showImage(sample)
    camera.release()


if __name__ == "__main__":
    main()

