# Be able to store multiple things on our clipboard
# import built in modules sys and json
# understand clipboard module
# files stored in json file (similar to python dictionary)

import sys
import clipboard
import json

saved_data = "clipboard.json" # name of file to store multi clipboard


# create a function that can create a json file
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data,f)

save_data("test.json", {"key":"value"}) # use to load keys and values

# build a function that reads json 
# if there is an error use try & except placed. if error occurs create an emppty dictionary
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}

if len(sys.argv) == 2:  # make sure only 2 command line argument, file name and command
    command = sys.argv[1]
    data = load_data(saved_data)
    
    # will need to create code that will save to clipboard 
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print("Data Saved")
    
    #if you want to ask for key, make sure key exists return error if not
    elif command == "load":
        key = input("Enter a Key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data Copied To Keyboard")
    
    # print out all the keys in ditionary
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command") 