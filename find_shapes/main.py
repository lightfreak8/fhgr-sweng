# import files
import cv2
from camera import Camera


def main():
    
    #for testing purposes implement camera class and test functions
    camera = Camera()
    img = camera.requestImage()
    camera.showImage(img)
    path = "C:/Users/rapha/switchdrive/PHO_Studium/Bildverarbeitung 2/4 Sensorcharakterisierung/material/westconcordorthophoto.png"
    sample = camera.requestSample(path)
    camera.showImage(sample)
    camera.release()



if __name__ == "__main__":
    main()

