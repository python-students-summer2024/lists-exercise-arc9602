from mood_assessor import *
import datetime

def main():    
    x = assess_mood()

    f = open('data/mood_diary.txt', 'a')
    f.write(str(x)+"\n")
    f.close()


main()