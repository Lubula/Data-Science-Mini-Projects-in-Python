# Assumptions:

# data directory contains many files and directories ( doing this manually not feasible )
# Only interested in the games contaiend in this directory
# each game is stored in a directory that contains the word "game"
# each game directory contains a single .go file that must be compiled before it can be run


# Project Steps/Requirements:

# Find all game directories from /data directory
# /data file loaded on repository simply download
# Create a new /games directory 
# Copy and remove the "game" suffix of all games into the /games directory
# Create a .json file with the information about the games
# Compile all of the game code 
# Run all of the game code-

# Step 1

# easier to put file in the same directory as the data . 
# import os for the operating system  files 
# import json for working with json file
# import shutil coipy and overwrite Process
# use subprocess , PIPE, to run any terminal commands to compoile and run go code
# import sys to access to command line arguments 

import os
import json
import shutil
from subprocess import PIPE, run
import sys

Game_Dir_Pattern = "game" # specifys what we looking for 
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]

# 4th Step
# Find all game directories from /data directory
# walk through the directory

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if Game_Dir_Pattern in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break

    return game_paths


# 6th step
# make a function trhat looks at the source_path just give directory name (strips path)

def get_name_from_path(paths,to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    return new_names


# 5th Step
# get the destination path
# create the new directory, check if it exists

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


# 7th step
# the source directory and targets has been done
# now we need to copy 
# if dir exist we overwrite,a recursive copy used here

def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


# 8th step 
# write a json with meta deta
# dirctory names and how many

def make_json_metadata_file(path, game_dirs):
    data = {
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }

    with open(path, "w") as f:
        json.dump(data, f)


# 9th step
# compile the code in directory and run it 

def complie_game_code(path):
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break

    if code_file_name is None:
        return

    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)



# 10th step
# runs any command , will need a path
# stdin = location whaere command is accepting input
# stdout = location whaere command is spitting output
# PIPE = makes a brige beween python code and process used toi run command. not a python built in command 

def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("compile result", result)

    os.chdir(cwd)



# 3rd step
# create a function with source and target to locate and add
# cwd = current working directory

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source) # always use this as diffrent operating systems path divides are diffrent
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_path(game_paths, "_game")
    create_dir(target_path)

    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        complie_game_code(dest_path)
    
    json_path = os.path.join(target_path, "Metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)

   
# 2nd step,
# find all game directory from data directory, create new directory with wanted data
# grab from command line argument what the source dicetory & target directory is relative to current path
# to know where to store and where to find data

if __name__ == "__main__":   # only want to execute main script if running file directly
    args = sys.argv
    if len(args) != 3 :
        raise Exception("You must pass a source and target directory- Only! ")
    
    source, target = args[1:]
    main(source, target)

