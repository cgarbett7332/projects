import time
import json

hours = float(input("please input time in hours"))
AverageSpeedList = []

List = AverageSpeedList

def AverageSpeed(hours):
    kilometer = 80
    speed = 80/hours
    print (speed)

#if AverageSpeed(hours) > int(48):
    #print("You broke the speed limit.")


AverageSpeedList = AverageSpeed(hours)
List.append(AverageSpeedList)
with open ("AverageSpeedList.txt",mode='w') as file:
        json.dump(List,file)

      








