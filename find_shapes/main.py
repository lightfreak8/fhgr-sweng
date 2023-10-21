"""
added code for testing class camera.py

"""


# import class
from camera import Camera

def main():
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

