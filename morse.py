import json # imports jSON python libraries

with open('ws.json', "r") as d: # opens jSON and loads it as data
    data = json.load(d)
    
    
while True: # forever loop
    option = input("Select, txt or morse: ").lower() # parses input from the user so correct option is chosen
    
    if option == "txt": # first option, user inputs text then morse code gets printed
        text_input = input("Enter your text: ").lower()
        morse = []
        for letter in text_input:
            if letter == " ":
                morse.append("/")
            elif letter in data:
                morse.append(data[letter])
            else:
                morse.append("?")
        print(" ".join(morse))
    elif option == "morse": # second option, user inputs morse code and then text gets printed
        morse_input = input("Enter your morse code: ")
        reverse = {v: k for k, v in data.items()}
        text = []
        for code in morse_input.split():
            if code == "/":
                text.append(" ")
            elif code in reverse:
                text.append(reverse[code])
            else:
                text.append("?")
        print("".join(text)) 
    elif option == "exit": # lets the user exit the app
        break
    else:
        print("Error, avaiable commands: txt ; morse") # error handling for options that fall out of the supported commands