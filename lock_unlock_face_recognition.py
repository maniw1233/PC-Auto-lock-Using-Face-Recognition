import cv2
import sys
import ctypes
import os

def assure_path_exists(path):
    """Ensure that the given path exists, create if it doesn't."""
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Initialize the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Ensure the trainer path exists
assure_path_exists("C:\\Users\\heman\\Downloads\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master\\trainer\\")

# Load the training model
recognizer.read('C:\\Users\\heman\\Downloads\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master\\trainer\\trainer.yml')

# Path to the face cascade
cascadePath = "C:\\Users\\heman\\Downloads\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master\\haarcascade_frontalface_default.xml"

# Load the face cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

# Set the font style for text in the video frame
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Initialize the webcam
cam = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    ret, im = cam.read()
    # Convert the frame to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)
        # Recognize the face and get the confidence level
        Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if confidence > 70:  # Unregistered face detected
            Id = "Unknown + {0:.2f}%".format(round(100 - confidence, 2))
            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 0, 255), -1)
            cv2.putText(im, str(Id), (x, y - 40), font, 1, (0, 0, 0), 2)

            # Lock the screen and stop
            cam.release()
            cv2.destroyAllWindows()
            ctypes.windll.user32.LockWorkStation()
            sys.exit()
        else:  # Registered face detected, continue displaying the webcam feed
            Id = "USER + {0:.2f}%".format(round(100 - confidence, 2))
            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (255, 255, 255), -1)
            cv2.putText(im, str(Id), (x, y - 40), font, 1, (0, 0, 0), 2)

    # Display the video frame with detected faces
    cv2.imshow('Webcam', im)

    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
