# Description
# this is the main driver which passes in each class from the robot module. 
# The driver will prompt user input of the robot and tresure (x,y) coodinates. 
# The user will also be able to move the robot North, South, East or West
#*******************************************************************************

import robot
from robot import robot
from robot import path
from robot import point

print("WELCOME TO GREEDY ROBOT") 
print("*********************************************************************************")


# assign int to x1 y1 x2 y2
x1, y1, x2, y2 = map(int, input("Please enter 4 coordinates for the location of the robot X Y, treasure X Y: " ).split())

# Coordinate to robot and tresure
r = path(x1, y1, x2, y2)
print("The location of the " + str(r)) 


move = input("\nTo move the robot enter (One of the following) \n 'N' = North\n 'S' = South \n 'E' = East\n 'W' West: \n ")
r.moveRobot(move)
print("The new location of the " + str(r)) 

print("\nList of Unique Paths" )
path.setPaths(r)
path.numUniquePaths(r)






