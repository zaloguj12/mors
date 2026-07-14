import json

with open('ws.json', "r") as d:
    data = json.load(d)
    
    
while True:
    option = input("Select, txt or morse: ").lower()
    
    if option == "txt": # done
        text_input = input("Enter your text: ").lower()
        morse = []
        for letter in text_input:
            if letter == " ":
                morse.append("/")
            elif letter in data:
                morse.append(data[letter])
            else:
                morse.append("?")
        print(" ".join(morse)) # should be outputting correctly for now
    elif option == "morse": # done
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
        print("".join(text)) # works good
    elif option == "exit": # done
        break
    else:
        print("Error, avaiable commands: txt ; morse")