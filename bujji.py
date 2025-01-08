import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

# Giving Voice Assistant Name 
va_name = 'leo'
# 
listener = sr.Recognizer()
speaker = pyttsx3.init()

# Giving rate of speed
rate = speaker.getProperty('rate')   # getting details of current speaking rate                       #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
def speak(text):
    speaker.say("Yes boss" + text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()
    
speak_ex("I am your" + va_name + 'Tell me boss')

def take_command():
    command = " "
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if va_name in command:
                command = command.replace(va_name + ' ', '')
                # print(command)
                # speak(command)
                
    except:
        print("Check your microphone")
    return command
while True:
    User_command = take_command()
    
    if 'close ' in User_command:
        print('See you again boss. I will be there for you ')
        speak('See you again boss. I will be there for you')
        break
    elif 'time' in User_command:
        cur_time= dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif "play" in User_command:
        User_command = User_command.replace("play ", '')
        print("Playing" + User_command)
        speak("Playing" + User_command + "Enjoy boss...")
        pk.playonyt(User_command)
        break
    elif 'search' in User_command or 'google' in User_command:
        User_command = User_command.replace("search for ",'')
        User_command = User_command.replace('google ','')
        User_command = User_command.replace('jarvis ','')
        # print("Searching for" + User_command)
        speak('Searching for' + User_command)
        pk.search(User_command)
    elif 'who is' in User_command or 'what is ' in User_command:
        User_command = User_command.replace('who is ', '')
        User_command = User_command.replace('what is ','')
        info = wiki.summary(User_command, 2)
        print(info)
        speak(info)
    elif "Who are you" in User_command:
        speak_ex("I am your" + va_name + 'Tell me boss')
    elif "What are you doing" in User_command:
        speak('I am Here to Help you')
        print("I am here to help you...")
    else:
       speak("Please say it again")
       print("Please say it again...")



# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import pywhatkit

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# def speak(text):
#     """Converts text to speech."""
#     engine.say(text)
#     engine.runAndWait()

# def greet_user():
#     """Greets the user based on the time of day."""
#     hour = datetime.datetime.now().hour
#     if hour < 12:
#         speak("Good morning! How can I assist you?")
#     elif hour < 18:
#         speak("Good afternoon! What can I do for you?")
#     else:
#         speak("Good evening! How may I help?")

# def listen_command():
#     """Listens to the user's voice command and returns it as text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.pause_threshold = 1  # Adjust pause if needed
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         command = recognizer.recognize_google(audio, language='en-in')
#         print(f"You said: {command}")
#         return command.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Please say it again.")
#         return ""
#     except sr.RequestError:
#         speak("Sorry, my speech service is down.")
#         return ""

# def handle_command(command):
#     """Handles the user's voice commands."""
#     if 'time' in command:
#         current_time = datetime.datetime.now().strftime('%I:%M %p')
#         speak(f"The time is {current_time}")
    
#     elif 'wikipedia' in command:
#         speak("What do you want to search on Wikipedia?")
#         query = listen_command()
#         if query:
#             result = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             speak(result)
    
#     elif 'open youtube' in command:
#         speak("Opening YouTube...")
#         pywhatkit.playonyt("trending videos")  # Opens YouTube in browser

#     elif 'play' in command:
#         song = command.replace('play', '').strip()
#         speak(f"Playing {song} on YouTube...")
#         pywhatkit.playonyt(song)

#     elif 'exit' in command or 'quit' in command:
#         speak("Goodbye! Have a great day.")
#         exit()

#     else:
#         speak("Sorry, I didn't understand that. Please try again.")

# if __name__ == "__main__":
#     greet_user()
#     while True:
#         user_command = listen_command()
#         if user_command:
#             handle_command(user_command)
