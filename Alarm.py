#A simple python program that allows the user to set an alarm
import time
import os
from datetime import datetime

def alarmSetup():
    '''This function displays the current time of the day and allows the user to set an alarm'''
    #displaying current time of the day
    now= datetime.now()
    current_time= now.strftime("%H:%M:%S")
    print("Today's time is", end =" ")
    print(current_time)
    hour = input("Enter the hour for the alarm > : ")
    minutes= input("Enter the minutes for the alarm > : ")
    secs = input("Enter the seconds for the alarm  > : ")

    if ((((int(hour) < 0 or int(hour)>24)) or (int(minutes) < 0 or int(minutes) > 60)) or (int(secs) < 0 or int(secs)> 60)):
        print(100*'.')
        print("invalid input:")

    else:
        print(100*'.')
        print("Alarm is successfully set at ", hour, ":", minutes, ":", secs)

def another_alarm():
    choice= input("Do you want to set another alarm? [y/n] ")
    mychoice = choice.lower()
    if mychoice=="y":
        alarmSetup()
    else:
        print("Alarm......")
        

alarmSetup()        
another_alarm()


    
    
