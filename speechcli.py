import speech_recognition as sr
import os

# Define your list of commands
commands = {
    "open file manager": "file_manager.py",
    "open browser": "browser.py",
    # Add more commands as needed
}

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_and_execute():
    print("Listening...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        
        # Check if the recognized command matches any predefined command
        if command in commands:
            program = commands[command]
            os.system(f"python {program}")
        else:
            print("No matching command found.")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Continuous listening loop
while True:
    listen_and_execute()
