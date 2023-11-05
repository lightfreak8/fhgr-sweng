"""
class_camera.py

class Camera:
for opening webcam, capturing image or loading sample by path and release camera in the end

changes:
1.0     2023-10-21      created
1.0.1   2023-10-21      public functions description added
1.1     2023-11-02      __init__: allow passing index
1.1.1   2023-11-05      add comments / descriptions

"""
import cv2

class Camera:
    """
    public functions:
    __init()__(self, index):        constructor, if not successfull set to None
    requestImage(self):             return cv2.Mat or None
    requestSample(self, path):      return cv2.Mat or None
    showImage(self, img)
    release(self)

    """

    #class contructor
    #open webcam and check if successfull
    def __init__(self, index=0):
        """
        constructor
        Args:
            index (int), camera index.

        """
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            print("Failed to open the webcam.")
            self.cap = None

    def requestImage(self):
        """
        Retrieves an image from the camera
        if not successfull returns None.
        Args:
            -
        Returns:
            frame, from the camera.
        
        """
        if self.cap is None:
            return None
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture an image from the webcam.")
            return None
        return frame     #returns cv2.Mat or None


    def requestSample(self,path):
        """
        Retrieves an image according to the path.
        if not successfull returns None.
        Args:
            path (string), where the sample is located.
        Returns:
            frame, according to path.
        
        """
        sample = cv2.imread(path)
        if sample is None:
            print(f"Failed to load image from path: {path}")
            return None
        return sample #returns cv2.Mat or None

    def showImage(self, img):
        """
        Shows an image.
        Args:
            frame to be displayed.
        
        """
        if img is None:
            print("invalid argument")
        cv2.imshow("Captured Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #release cam
    def release(self):
        """
        Closes capturing device.
        
        """
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
