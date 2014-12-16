#this file contains all the functions required for guess who
#gets a picture of the user

import picamera
import time
import json


            
def getUserImage(name):

    try:
        check=False
        while check == False:
            with picamera.PiCamera() as camera:
                camera.start_preview()
                time.sleep(2)
                filename = "{0}_img.jpg".format(name)
                camera.capture(filename)
                camera.stop_preview()
                time.sleep(1)
        
            correct=input("Your picture is named {0}.Are you happy with that picture?".format(filename))
            if correct.lower()=="yes":
                check = True
                return filename
    except picamera.exc.PiCameraMMALError:
        print("Camera not detected,please connect and restart")
        filename=""


def getCharProfile():
    #name
    check = False
    while check == False:
        Fname = input("What is your first name?")
        correct = input("Your first name is {0}, is that correct?".format(Fname))
        if correct.lower()=="yes":
            check = True
    filename = getUserImage(Fname)
    #hair colour
    check=False
    while check == False:
        hair = ""
        while not(hair in ["black","blond","brown","ginger"]):
            hair = input("what is your hair colour?")
        correct = input("your hair is {0}, is that correct?".format(hair))
        if correct.lower()=="yes":
            check = True
    #eye colour
    check=False
    while check == False:
        eye = ""
        while not(eye in ["blue","brown","green"]):
            eye = input("what is your eye colour?")
        correct = input("your eyes is {0}, is that correct?".format(eye))
        if correct.lower()=="yes":
            check = True
    #glasses
    glasses = input
    if input = 

    
        

    



    return [Fname, filename, hair, eye]





def LoadData():
    try:
        with open ("PeopleData",mode='r') as file:
            people = json.load(file)
    except IOError:
        print("ERROR")
        people=[]
    return people

def StoreData():
    person = getCharProfile()
    people.append(person)
    with open ("PeopleData",mode='w') as file:
        json.dump(people,file)


    
people = LoadData()
StoreData()
