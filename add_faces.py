import cv2
import pickle                               # Used to store data in .pkl file i.e. in the text format.
import cv2.data
import numpy as np                          # for creating numpy array. 
import os                                   # Used for creating files or reading files.

if not os.path.exists('data/'):       # for checking data folder is present or not.
    os.makedirs('data/')              # If data folder is not there then create it.

video = cv2.VideoCapture(0)           # Opening web camera.
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')   # Trained model for face detection by opencv.
faces_data = []     # faces data array to store images.

i = 0
name = input("Enter Aadhaar: ")
framesTotal = 51          # Total images that will be clicked.
captureAfterFrame = 2     # To keep a pause between frames.

while True:
    ret, frame = video.read()                          # Start/Read the video.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # Converting to gray scale.
    faces = facedetect.detectMultiScale(gray, 1.3, 5)       # taking frame and detecting face.
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]                   # Cropping the face out of large image.
        resized_img = cv2.resize(crop_img, (50, 50))             
        if len(faces_data) <= framesTotal and i%captureAfterFrame == 0:    # going upto framestotal value which was initialized earlier and for every second frame we are capturing.
            faces_data.append(resized_img)        # Appending the resized image in faces data array. 
        i = i+1
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)    # To add face count on the capturing screen.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)       # For rectangle around the face we are doing this.

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) >= framesTotal:
        break

video.release()
cv2.destroyAllWindows()

# print(faces_data)

faces_data = np.asarray(faces_data)         # Creating numpy array for storing data.
faces_data = faces_data.reshape((framesTotal, -1))

# print(faces_data)

if 'names.pkl' not in os.listdir('data/'):      # Checking for names.pkl inside data forder If not exist then create it.
    names = [name]*framesTotal                  # According to the frames just get the names.
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)                    # save/dump those names.
else:                                              
    with open('data/names.pkl', 'rb') as f:        # If file already exist then open this file, read the file.   
        names = pickle.load(f)                     # load the data.
    names = names + [name]*framesTotal              # appending new data.
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)                      # save the data.


if 'faces_data.pkl' not in os.listdir('data/'):      #Checking for faces.pkl inside data forder if not exist then create it.
    with open('data/faces_data.pkl', 'wb') as f:     
        pickle.dump(faces_data, f)                    # save the face data.
else:  
    with open('data/faces_data.pkl', 'rb') as f:      # If already exist then open this file, read this file.
        faces = pickle.load(f)                        # load the data.
    faces = np.append(faces, faces_data, axis = 0)    # append new data.
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)                          # save/dump the data.


