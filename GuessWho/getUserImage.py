#this file contains all the functions required for guess who

import picamera # this imports picamera so it can use the camera to take pictures
import time # this imports the time commands e.g. time.sleep(2)
import json # imports json which is slightly different to python. it is abit like pickle but python understands it.
        
def getUserImage(name): # this defines the function getUserImage which takes a picture

    try:
        check=False
        while check == False:
            with picamera.PiCamera() as camera:
                camera.start_preview() # this starts a preview of what the camera is seeing so you know what the picture will look like
                time.sleep(2)
                filename = "{0}_img.jpg".format(name)
                camera.capture(filename) # this takes the picture
                camera.stop_preview() # this stops the preview of the picture
                time.sleep(1)
        
            correct=input("Your picture is named {0}.Are you happy with that picture?".format(filename))
            if correct.lower()=="yes": # if the user says yes, it will start to ask the questions, if not, it will take a picture again until you are happy with it
                check = True
                return filename
    except picamera.exc.PiCameraMMALError: # if this error comes up (if you don't have your camera plugged in), instead it will say to the user that there is no camera connected
        print("Camera not detected,please connect and restart")
        filename=""

def getCharProfile(): # this code defines the function getCharProfile
    #name
    check = False
    while check == False:
        Fname = input("What is your first name?") # this will ask the user what their first name is
        correct = input("Your first name is {0}, is that correct?".format(Fname))
        if correct.lower()=="yes": # if the user says yes, it will go to the next question, if not, it will ask what their first name is again
            check = True

    filename = getUserImage(Fname)

    # this part asks what your hair colour is
    hair = ""
    while not(hair in ["black","blond","brown","ginger"]): # if the input isn't any hair colours on this list, it will ask the question again until it is
        hair = input("What is your hair colour?") # this will ask the user what their hair colour is

    # this part asks about your eye colour 
    eye = ""
    while not(eye in ["blue","brown","green"]): # if the input isn't in this list, it will ask again until it is.
        eye = input("What is your eye colour?") # this will ask the user what their eye colour is.
        
    # this part asks if you have glasses or not
    glasses = ""
    while not(glasses in ["yes","no"]):
        glasses = input("Do you wear glasses?")

    # this part asks what you gender is
    gender = ""
    while not(gender in ["male","female"]):
        gender = input("What is your gender?")

    # this part asks if you wear a hat or not
    hat = ""
    while not(hat in ["yes","no"]):
        hat = input("Do you wear a hat?")

    # this part asks if you have any facial hair
    facial_hair = ""
    while not(facial_hair in ["yes","no"]):
        facial_hair = input("Do you have any facial hair?")
       
        
    return [Fname, filename, hair, eye, glasses, gender, hat, facial_hair]

def LoadData(): # this defines the function LoadData()
    try:
        with open ("PeopleData",mode='r') as file: # this opens the file in read mode
            people = json.load(file)
    except IOError:
        print("ERROR")
        people=[]
    return people

def StoreData(): # this defines the function StoreData()
    person = getCharProfile()
    people.append(person)
    with open ("PeopleData",mode='w') as file: # this opens the file in write mode
        json.dump(people,file)
   
people = LoadData()
print(people)
while len(people)<24:
    StoreData()
    print("captured")
