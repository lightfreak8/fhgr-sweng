"""
class_camera.py

class Camera:
for opening webcam, capturing image or loading sample by path and release camera in the end

changes:
1.0     2023-10-21      created
1.0.1   2023-10-21      public functions description added

public functions:
    __init()__(self):   constructor, if not successfull set to None
    requestImage():     return cv2.Mat or None
    requestSample(string path):    return cv2.Mat or None
    showImage(cv2.Mat img)
    release()




"""
import cv2

class Camera:
    #class contructor
    #open webcam and check if successfull
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Failed to open the webcam.")
            self.cap = None
    
    def requestImage(self):
        if self.cap is None:
            return None
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture an image from the webcam.")
            return None
        return frame     #returns cv2.Mat or None
    

    def requestSample(self,path):
        sample = cv2.imread(path)
        if sample is None:
            print(f"Failed to load image from path: {path}")
            return None
        return sample #returns cv2.Mat or None
    
    def showImage(self, img):
        image = self.requestImage()
        if image is None:
            print("invalid argument")
        cv2.imshow("Captured Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #release cam
    def release(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

# Example usage:
# if __name__ == "__main__":
#     camera = Camera()
#     img = camera.requestImage()
#     camera.showImage(img)
#     path = "C:/Users/rapha/switchdrive/PHO_Studium/Bildverarbeitung 2/4 Sensorcharakterisierung/material/westconcordorthophoto.png"
#     sample = camera.requestSample(path)
#     camera.showImage(sample)
#     camera.release()
