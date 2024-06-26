import datetime
import os, time


def assess_mood():
    if last_modified_fileinfo('data/mood_diary.txt') == str(datetime.date.today()):
        print("Sorry, you have already entered your mood today.")
        return
    mood = ask_for_mood()
    while mood not in ["happy","relaxed","apathetic","sad","angry"]:
        mood = ask_for_mood()
    if mood == "happy":
        x = False
        today_mood = mood
        return 2
    elif mood == "sad":
        x = False
        today_mood = mood
        return -1
    elif mood == "relaxed":
        x = False
        today_mood = mood
        return 1
    elif mood == "apathetic":
        x = False
        today_mood = mood
        return 0
    elif mood == "angry":
        x = False
        today_mood = mood
        return -2
        

def last_modified_fileinfo(filepath):
    # Get the file status using os.stat() function
    filestat = os.stat(filepath)
    # Get the last modified date and time in local time
    date = time.localtime((filestat.st_mtime))

    # Extract year, month, and day from the date
    year = date[0]
    month = date[1]
    day = date[2]
    hour = date[3]
    minute = date[4]
    second = date[5]
    strYear = str(year)[0:]
    if (month <=9):
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)
    if (day <=9):
        strDay = '0' + str(day)
    else:
        strDay = str(day)
    return (strYear+"-"+strMonth+"-"+strDay)
        
    



        
            

    

def ask_for_mood():
    mood = input("Hello! How do you feel today? Please pick from the following options: \n Happy \n Relaxed \n Apathetic \n Sad \n Angry ")
    return mood