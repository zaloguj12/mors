import json # imports jSON python libraries

with open('ws.json', "r") as d: # opens jSON
    data = json.load(d) # loads the jSON as data
    
    
while True: # forever loop
    option = input("Select: txt or morse: ").lower() # parses input from the user so correct option is chosen
    
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
    elif option == "exit": # lets the user exit the app
        break # stops the app
    else: # else...
        print("Error, avaiable commands: txt ; morse") # error handling for options that fall out of the supported commands