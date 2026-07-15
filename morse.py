import json # imports jSON python libraries
import numpy as np # import fancy science stuff
from scipy.io import wavfile # import a way to save sound
import os # import operating systemation
import sys # import the system itself

if getattr(sys, "frozen", False): # make sure github doesnt shit itself
    base_path = sys._MEIPASS # lowkey toilet
else: # else...
    base_path = os.path.dirname(__file__) # lowkier toilet

json_path = os.path.join(base_path, "ws.json") # find jSON

with open(json_path) as d: # open jSON
    data = json.load(d) # load jSON
    
while True: # forever loop
    option = input("Select: txt or morse or audio: ").lower() # parses input from the user so correct option is chosen
    
    if option == "txt": # first option, user inputs text then morse code gets printed
        text_input = input("Enter your text: ").lower() # capture user input and make it lowercase
        morse = [] # a list
        for letter in text_input: # a for loop to properly display all characters
            if letter == " ": # proper splitting
                morse.append("/") # proper splitting
            elif letter in data: # actual reading
                morse.append(data[letter]) # writing to list
            else: # else...
                morse.append("?") # error catching
        print(" ".join(morse)) # display of text
    elif option == "morse": # second option, user inputs morse code and then text gets printed
        morse_input = input("Enter your morse code: ") # capture user input
        reverse = {v: k for k, v in data.items()} # reverse the jSON
        text = [] # a list
        for code in morse_input.split(): # a for loop to display the whole morse code
            if code == "/": # proper splitting
                text.append(" ") # proper splitting
            elif code in reverse: # actual reading
                text.append(reverse[code]) # writing to list
            else: # else...
                text.append("?") # error catching
        print("".join(text)) # display of morse code
    elif option == "audio": # thrid option, user inputs morse code and it gets converted to a .wav file for listening
        audio_input = input("Enter your morse code: ") # capture user input
        sample_rate = 44100 # set the sample rate
        frequency = 700 # freq in Hz
        unit = 0.1 # units in seconds
        def tone(duration): # function for actuall audio
            t = np.linspace(0, duration, int(sample_rate * duration), False) # calculate sound
            return np.sin(2 * np.pi * frequency * t) # return sound
        def silence(duration): # function for silence
            return np.zeros(int(sample_rate * duration)) # return silence
        audio = [] # a list
        for char in audio_input: # a for loop to convert all
            if char == ".": # if . then single sound
                audio.append(tone(unit)) # add sound to list
                audio.append(silence(unit)) # add silence to list
            elif char == "-": # if - then triple sound
                audio.append(tone(unit * 3)) # add triple sound to list
                audio.append(silence(unit)) # add silence to list
            elif char == " ": # if null add double silence
                audio.append(silence(unit * 2)) # add double silence to list
            elif char == "/": # if / then sixtuple silence
                audio.append(silence(unit * 6)) # add sixtuple silence to list
        audio = np.concatenate(audio) # make audio equal concatenate of audio
        audio = np.int16(audio * 32767) # change audio to 16 bit
        wavfile.write("morse.wav", sample_rate, audio) # write to file
        print("is saved as sound morse.wav") # display sucesful sound write
    elif option == "exit": # lets the user exit the app
        break # stops the app
    else: # else...
        print("Error, avaiable commands: txt ; morse") # error handling for options that fall out of the supported commands