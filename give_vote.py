from sklearn.neighbors import KNeighborsClassifier      # Using KNN classifier from sklearn package for face comparison.
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(str1):                      # function used for text to speech conversion.
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)           # with Sapivoice speak the text provided in str1.

video = cv2.VideoCapture(0)      # Capture the webcam.
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')   # trained medel for face detection . 

if not os.path.exists('data/'):               # for checking data folder is present or not.
    os.makedirs('data/')                      # If data folder is not there then create it.

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)              # load the names.

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)               # load the faces.

knn = KNeighborsClassifier(n_neighbors=5)          # We are looking for nearest five neighbours for particular face.

knn.fit(FACES, LABELS)            # Fitting the face with labels i.e. aadhar no.

imgBackground = cv2.imread("Voting.jpg")        # Loading the background image.

COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']      # Storing the data in the form of table in votes.csv file.

while True:
    ret, frame = video.read()          # Reading frame from webcam.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        # Converting to gray scale.
    faces = facedetect.detectMultiScale(gray, 1.3, 5)     # face detection.
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]        # crop the image to get specific face part.
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)       # Resizing image to 50*50 pixel.
        output = knn.predict(resized_img)       # Providing the image to knn model.
        ts = time.time()               # Storing time also.
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%y")      # For timestamp. 
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")     # Storing date.
        exist = os.path.isfile("Votes" + ".csv")          # Checking for votes.csv.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)      # Creating a rectangle around our face.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        attendance = [output[0], timestamp]     # Storing vote and timestamp.
    
    imgBackground = frame        # To show camera window over our background image.
    
    cv2.imshow('frame', imgBackground)
    k = cv2.waitKey(1)

    def check_if_exists(value):               # To check if already voted or not.
        try:
            with open("Votes.csv", "r") as csvfile:         # opening votes.csv
                reader = csv.reader(csvfile)                 # Read csv file.
                for row in reader:
                    if row and row[0] == value:          # findind the value in each row.   
                        return True                       # if present then return true.
        except FileNotFoundError:
            print("File not found or unable to open the CSV file.")
        return False           # If not already exist then return false.
    
    voter_exist = check_if_exists(output[0])
    if voter_exist:
        print("YOU HAVE ALREADY VOTED")     
        speak("YOU HAVE ALREADY VOTED")      # if already voted then you will get this voice text.
        time.sleep(10)
        break
    if k == ord('1'):
        speak("YOUR VOTE HAS BEEN RECORDED")     # Pressed 1 and vote gets recorded.
        time.sleep(10)
        if exist:        
            with open("Votes" + ".csv", "+a") as csvfile:         # If votes.csv exist then open votes.csv
                writer = csv.writer(csvfile)
                attendance = [output[0], "BJP", date, timestamp]      # writing thet which party you have voted and all other details.
                writer.writerow(attendance)
            csvfile.close()             # close the csv file.
        else:   
            with open("Votes" + ".csv", "+a") as csvfile:          # If votes.csv doesnt exist then this code will be executed.
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "BJP", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

    if k == ord('2'):                        # Similarly for other parties we can add data.
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(10)
        if exist:
            with open("Votes" + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "CONGRESS", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes" + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "CONGRESS", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

    if k == ord('3'):
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(10)
        if exist:
            with open("Votes" + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "AAP", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes" + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "AAP", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

    if k == ord('4'):
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(10)
        if exist:
            with open("Votes" + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "NOTA", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes" + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "NOTA", date, timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

video.release()       # After storing votes closing the webcam.
cv2.destroyAllWindows()
    
    
