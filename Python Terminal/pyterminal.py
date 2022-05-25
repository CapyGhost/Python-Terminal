import os
import pyttsx3
import time
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print(
"""
Python Terminal - By Shadow King(Sanketh Somaiah)

No CopyRights
Compleate Open Source :)
type 'help' for commands

""")

while True:
    terminal = input("python_venv\\terminal>")
    
    if terminal == "help":
        print(
        """
        All Windows Terminal Commands
        'tts' -  enables text to speech (need's tts addon to be installed)
        'time' - shows time
        
        """)
    
    elif terminal == 'tts':
        tts_runtime = True
        print("type 'exit' to exit the tts")
        while tts_runtime:
        
            tts = input("\npython_venv\\terminal\\tts>")
            if tts == 'exit':
                print("Exiting tts...")
                tts_runtime = False
                time.sleep(1)
                print("\nexited tts")
            
            else:
                speak(tts)

    elif terminal == 'time':
        print(f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}")


    else:
        os.system(terminal)
    
