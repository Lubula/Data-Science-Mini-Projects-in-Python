# Step 2
# use built in module called turtle , great for basics. Will create the screen 2D graph
# working with graphics requires defining the width and the height of the turtle screen

import time
import turtle
import random

WIDTH, HEIGHT = 500, 500  # these are constant values, usually use all capital letter. never change
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown","cyan"]

# step 1
# get input of the number of turtles the user wishes to  see race 10 maximum turtles
# create a function that will generate the number of turtles the user wants to have
# make sure the input from user is converted to numeric (interger). use the .isdigit() method

def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Enter The Number of Turtles Racing (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not Numeric... Try again")
            continue        # this continue makes you jump back to the while loop

        if 2<= racers <=10:
            return racers
        else:
            print("Number not in 2-10 Range. Try again")

# test the code if function is working its working 
# racers = get_number_of_turtles()
# print(racers)

# STEP 6
# create a new funbtion to take in colors 

def race(colors):
     turtles = create_turtle(colors)

     while True:
          for racer in turtles:
               distance = random.randrange(1,20)
               racer.forward(distance)

               x, y = racer.pos()
               if y >= HEIGHT // 2- 10:
                    return colors[turtles.index(racer)]

# STEP 5
# create a new function 
# create a list of turtles, that will be placed on screen in starting position ready to start racing
# turtles must be evenly placed out and ready to begin pointing upward
# firstly determine what colors they are and how many turtles there are
# create a empty list, then loop through colors, for each color create a turtle & add to empty list
# create tutrle object and add color. shape, set position & direction. google "turtle python"
# figure out spacing of turtles using set position (.setpos()) . understand y & x axis

def create_turtle(colors):
     turtles = []
     spacingx = WIDTH // (len(colors) +1 )
     for i, color in enumerate(colors):
          racer = turtle.Turtle()
          racer.color(color)
          racer.shape("turtle")
          racer.left(90)
          racer.penup()
          racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 +20)
          racer.pendown()
          turtles.append(racer)

     return turtles


# step 3 
# everything related to the turtle screen (screen dimentions, set up and name)
# firstly get the number of racers then run the turtle screen
 
def init_turtle():
        screen = turtle.Screen()
        screen.setup(WIDTH, HEIGHT) 
        screen.title("Turtle Racing!")

racers = get_number_of_turtles()
init_turtle()

# STEP 4
# add colors list at top
# take list and randomise it, select 1st of racers item 
# slice operator to get the elemenst needed

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The Winnner Is The Turtle With Color:", winner)
time.sleep(5)


# turtorial step 4. please go to turtle python on google. There is a list of stuff that can be done 
# to move the turtle we must create a turtle object
# use the time module to stop application from closing to see the change in direction

# racer = turtle.Turtle()
# racer.speed(2)
# racer.shape("turtle")
# racer.color("cyan")
# racer.penup()
# racer.forward(100)
# racer.left(30)
# racer.pendown()
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
# time.sleep(2)
