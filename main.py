#importing libs for functions later
import speech_recognition as sr   #bones of the program
import datetime  # for what time it is
import wikipedia #allows person to search for people
import pyjokes  #funny
import random
import time as time


#setting up the libs for useage
engine = pyttsx3.init()
listener = sr.Recognizer()
#defs for useage later (makes it easier)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def input_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        print("error!!!")
    return command


#MAIN

def run_jarvis():  # main code it will be running through
    command = input_command()
    print(command)
    #prints the time and says it
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    #says who the person is from wikipedia
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif "random number" in command:
        num=random.randint(0,10)
        num=str(num)
        speak(num)
        print(num)
    elif "joke" in command:#there is 2 types of jokes, ones from pyjokes lib and my own custom ones
        joke_type=random.randint(1,2)#using a random generator to randomly choose from a catagory
        if joke_type == 1:#pyjokes
          speak(pyjokes.get_joke())
        elif joke_type == 2:
            joke_num=random.randint(1,4)#increase the "4" to how many there is
            if joke_num==1:
                speak("there is no funny")
                print("there is no funny")
            if joke_num==2:
                speak("a packet of crisps was walking down the road, a van pulled up")
                print("a packet of crisps was walking down the road, a van pulled up")
                time.sleep(0.3)
                speak(" want a lift?nah im walkers")
                print("want a lift?nah im walkers")
            if joke_num==3:
                speak("everyones a gangster till i have no jokes left ")
                print("everyones a gangster till i have no jokes left ")
            if joke_num==4:
                speak("daughther writes with her left hand and is smart")
                print("daughther writes with her left hand and is smart")
                time.sleep(0.4)
                speak("14th century dad witch")
                print("14th century dad witch")
    elif "dead by daylight joke"in command:#dedicated jokes for a game i love playing at the moment
        jnum=random.randint(1,4)#jnum == joke number
        if jnum==1:
            speak("dbd players realizing they can loop the killer who just broke into there house")
            print("dbd players realizing they can loop the killer who just broke into there house")
            speak("person dancing")
            print("*dancing gif*")
        elif jnum==2:
            speak("dwight")
            print("dwight")
        elif jnum==3:
            speak("devs looking at the doctor *cough* balance *cough* update like")
            print("devs looking at the doctor balance update like")
            time.sleep(0.2)
            speak("that sign cant stop me cause i cant read")
            print("that sign can't stop me cause i can't read")
        elif jnum==4:
            print("dbd devs after releasing legion")
            speak("dbd devs after releasing legion")
            speak(" i think we did a pretty good job so far")
            print((" i think we did a pretty good job so far"))
    elif "turn off" or"shutdown" in command:#exit program
        speak("powering down")
        exit()
    elif "rick roll" in command:
        speak("We're no strangers to loooooove")#
        time.sleep(0.3)
        speak("know the rules and so do I A full commitment's what I'm thinking of")
        time.sleep(0.3)
        speak("You wouldn't get this from any other guy")
        time.sleep(0.2)
        speak("I just wanna tell you how I'm feeling")
        time.sleep(0.3)
        speak("Gotta make you understand")
        time.sleep(0.4)
        speak("neva gonna give you up neva gonna let you doooowwwnnnn")
    elif "bedtime story" in command:
        speak("playing bed time stories")
        random_story=random.randint(1,2)
        if random_story==1: # ragnar the red
            speak("playing ragnar the red")
            print("playing ragnar the red")
            print("Oh, there once was a hero named Ragnar the Red Who came riding to Whiterun from ole Rorikstead And the braggart did swagger and brandish his blade As he told of bold battles and gold he had made")
            speak("Oh, there once was a hero named Ragnar the Red Who came riding to Whiterun from ole Rorikstead And the braggart did swagger and brandish his blade As he told of bold battles and gold he had made")
            print("But then he went quiet, did Ragnar the Red When he met the shieldmaiden Matilda who said Oh, you talk and you lie and you drink all our mead Now I think it's high time that you lie down and bleed")
            speak("But then he went quiet, did Ragnar the Red When he met the shieldmaiden Matilda who said Oh, you talk and you lie and you drink all our mead Now I think it's high time that you lie down and bleed")
            speak("And so then came clashing and slashing of steel As the brave lass Matilda charged in full of zeal And the braggart named Ragnar was boastful no more ")
            print("And so then came clashing and slashing of steel As the brave lass Matilda charged in full of zeal And the braggart named Ragnar was boastful no more ")
            time.sleep(0.4)
            print("When his ugly red head rolled around on the floor")
            speak("When his ugly red head rolled around on the floor")
        if random_story==2:
            speak(" there once was a goat")
            print("there once was a goat")
            speak(" he lived in peace ")
            print("he lived in peace")
            speak(" the end")
            print("the end")
