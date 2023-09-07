# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.
#
# Your program should print out the result of
# your two sense measurements.



from math import *
import random
import robot

landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]]
world_size = 100.0

def eval(r, p):
    sum = 0.0;
    for i in range(len(p)): # calculate mean error
        dx = (p[i].x - r.x + (world_size/2.0)) % world_size - (world_size/2.0)
        dy = (p[i].y - r.y + (world_size/2.0)) % world_size - (world_size/2.0)
        err = sqrt(dx * dx + dy * dy)
        sum += err
    return sum / float(len(p))

####   DON'T MODIFY ANYTHING ABOVE HERE! ENTER CODE BELOW ####

myrobot = robot.robot()
myrobot.set(30, 50, pi/2)
# forward_noise = 5.0, turn_noise = 0.1,
# sense_noise = 5.0.
myrobot.set_noise(5.0, 0.1, 5.0)


myrobot = myrobot.move(pi/2, 15) #we have reassign the myrobot variable
sensing1 = myrobot.sense()
myrobot = myrobot.move(pi/2, 10)
sensing2 = myrobot.sense()

print(sensing1)
print(sensing2)