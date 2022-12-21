#There are 38 slots for the ball on the roulette table in the casino: 18 red,
# the same number of black and two green, numbered 0 and 00, respectively. 
#Red numbers on roulette: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36.
# The remaining numbers in the range of positive numbers up to 36 are black. The player 
# can make a variety of bets. In this exercise we will consider only the following types of bets:
# one number (from one to 36, as well as 0 or 00);
# red or black;
# even or odd (note that the numbers 0 and 00 are neither even nor odd);
# from 1 to 18 vs from 19 to 36.
#Write a program simulating a roulette game using a random number generator in Python. 
#After starting the roulette, display the number that has fallen out and all the bets that have played.


import random

"""All nums"""
red_nums = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34]
black_nums = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33]
all_colors = [0,00,1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32
            ,34,2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33]
win_num = random.choice(all_colors) #bet won
color = [] #winner color
divide = [] #winner divide
numbering = [] #winner numbering

def Game():
    """imitation game"""
#Red of black
    if win_num in red_nums:
        color.append("red")
    if win_num in black_nums:
        color.append("black")
#Divide
    if win_num%2<=0:
        divide.append('even')
    else:
        divide.append('uneven')
#Numbering
    if win_num<=18:
        numbering.append('from 1 to 18')
    else:
        numbering.append('from 18 to 34')
    print ("On table: " + str(win_num) + "...")
    print ("The bet won: " + str(win_num) )
    print ("The bet won: " + "".join(color))
    print ("The bet won: " + "".join(divide))
    print ("The bet won: " + "".join(numbering))

def Zero():
    """search for zeros"""
    if win_num==00:
        print ("On table: " + str(win_num))
        print ("The bet won: " + str(win_num))
        exit()
    if win_num==00:
        print ("On table: " + str(win_num))
        print ("The bet won: " + str(win_num))
        exit()
    if win_num>0:
        Game()

Zero()