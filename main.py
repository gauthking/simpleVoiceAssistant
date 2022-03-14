# install pyaudio by using any of the two commands below
# 1 - 'pip install pyaudio' (if you are using versions 3.7 or below)
# 2 - 'py -m pipwin install pyaudio' (if you are using higher python version like 3.9 or above, also make sure the pipwin package manager is installed first using the 'pip install pipwin')

# install the packages below and import them :
# pyttsx3 - 'pip install pyttsx3'
# speech_recognition - 'pip install speechRecognition'
# datetime - will be pre installed in the system, so just import it


from django.dispatch import receiver
import pyttsx3
import speech_recognition as spr
import datetime
import random
import wikipedia
from pywhatkit import playonyt
import smtplib

# enter your name
name = "Gautham"
voice_engine = pyttsx3.init('sapi5')
voices = voice_engine.getProperty('voices')
print(voices)
voice_engine.setProperty('voice', voices[1].id)
voice_engine.setProperty("rate", 145)


def speak(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()


def initializeruby():
    c = spr.Recognizer()
    with spr.Microphone() as src:
        c.pause_threshold = 1
        aud = c.listen(src)
        print("Engine is listening")
        query = c.recognize_google(aud, language='en-in')
        print(f"{name} said : ", query)
    return query


def tcommand():
    c = spr.Recognizer()
    with spr.Microphone() as src:
        print("Ruby is listening...")
        c.pause_threshold = 1
        aud = c.listen(src)
    try:
        print("Ruby is Processing..")
        query = c.recognize_google(aud, language='en-in')
        print(f"{name} said : ", query)

    except Exception as e:
        print("Say that again please..")
        tcommand()
        return "None"
    return query


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(f"Good Morning {name}. It is {hour} AM\n")
        speak(f"Good Morning {name}. It is {hour} AM")
    elif hour >= 12 and hour <= 16:
        print(f"Good Afternoon {name}. It is {hour} PM\n")
        speak(f"Good Afternoon {name}. It is {hour} PM")
    else:
        print(f"Good Evening {name}. It is {hour} PM\n")
        speak(f"Good Evening {name}. It is {hour} PM")

    speak(f"Hope you having a good day! I'm Ruby, How can I help you {name}\n")
    tcommand()


def greet():
    greetlist = ["I'm doing good", "I'm fine",
                 "It's a great day today, I'm doing fine, I hope you are too!"]
    r = random.choice(greetlist)
    print(r)
    speak(r)


def wiki(info, lines):
    result = wikipedia.summary(info, sentences=lines)
    return result

def playmusic(link):
    try:
        playonyt(link)
        print("Playing Now...")
        speak("Playing Now...")
    except:
        print("Network Error Occured... Please Make sure you are connected to the internet..")
        speak("Network Error Occured... Please Make sure you are connected to the internet..")

def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    speak("Enter your mail ID and password below")
    print("Enter your mail ID and password below")
    mailid = input()
    passwd = input()
    server.login(mailid, passwd)
    server.sendmail(mailid, to, content)
    server.close()



if __name__ == "__main__":
    init = initializeruby().lower()
    if "ruby" in init:
        print("Voice Assistant Activated")
        speak(f"Hello I'm ruby how can I help you {name}")
        while True:
            cmd = tcommand().lower()
            if "time" in cmd:
                wishme()

            elif "how are you" in cmd:
                greet()

            elif "wikipedia" in cmd:
                cmd1 = cmd.replace("wikipedia", "")
                print(cmd1)
                print(wiki(cmd1, 2))
                speak(wiki(cmd1, 2))
                print("Would you like to listen more about this result ? (Yes/No)")
                speak("Would you like to listen more about this result ?")
                m = tcommand().lower()
                if m == "yes":
                    print(wiki(cmd1, 7))
                    speak(wiki(cmd1, 7))

            elif "youtube" in cmd:
                cmd2 = cmd.replace("youtube", "")
                playmusic(cmd2)
                break

            elif "hey" in cmd:
                speak(f"Hey. How can I help you {name}")

            elif "exit" in cmd: 
                exit
            
            ## email sending features require to enable IMAP/POP in your GMAIL account settings and also disable some vulnerability settings in your google account which is not recommended. So I have commented out the email sending feature, if you want to test feel free to uncomment the below elif statement and try it out.
            
            # elif "email" in cmd:
            #     try:    
            #         print("To whom do you want to send the email to ? ")
            #         speak("To whom do you want to send the email to ? ")
            #         print("Enter the reciever Mail Id : ")
            #         recv = input()
            #         print("Okay! What do you want me to say ? ")
            #         speak("Okay! What do you want me to say ? ")
            #         mail = tcommand()
            #         sendemail(recv, mail)
            #         speak("Your mail has been sent")
            #         print("Your mail has been sent")
            #     except Exception as e:
            #         print(e)
            #         print("Unknown Network error occured. Please try again later")
            #         speak("Unknown Network error occured. Please try again later")




            else:
                speak("I didn't get you, Please repeat that again")

    else:
        print("Not activated.. Run the program again")
