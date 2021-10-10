import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()  # this help to recognize your voice
engine = pyttsx3.init() # make obj of pyttsx3
voices = engine.getProperty('voices')   # adding all voices in voices variable
engine.setProperty('voices', voices[1].id)

def talk(text):
    # this help to the repeat the command
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        # listen from your microphone
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # use for the search voice on google
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', "")  # replace alexa word with nothing
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()    # calling take_command function
    if 'play' in command:
        song = command.replace('play', '')  # here play word replace by nothing
        talk('playing' + song)  # pass string to the talk function
        pywhatkit.playonyt(song)

    elif 'time' in command : # alexa tell me the time
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'wikipedia' in command:
        search = command.replace('wikipedia', '')
        info = wikipedia.summary(search,1)
        print(info)
        talk(info)

    elif 'joke' in command :
        talk(pyjokes.get_joke())

# calling run_alexa function
run_alexa()

