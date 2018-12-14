import time

from logic import *

def canLeft(game):
    for i in game:
        if i[0] == 0 and (i[1]!=0 or i[2]!=0 or i[3]!=0):
            return True
        elif i[1] == 0 and (i[2]!=0 or i[3]!=0):
            return True
        elif i[2] == 0 and i[3]!=0:
            return True
        elif i[0] == i[1] or i[1] == i[2] or i[2] == i[3] :
            return True
    return False
def canRight(game):
    for i in game:
        if i[3] == 0 and (i[2]!=0 or i[1]!=0 or i[0]!=0):
            return True
        elif i[2] == 0 and (i[1]!=0 or i[0]!=0):
            return True
        elif i[1] == 0 and i[0]!=0:
            return True
        elif i[0] == i[1]and i[0]!=0 or i[1] == i[2] and i[1]!=0 or i[2] == i[3] and i[2]!=0 :
            return True
    return False
def canUp(game):
    for i in range(3):
        if game[0][i] == 0 and (game[1][i]!=0 or game[2][i]!=0 or game[3][i]!=0):
            return True
        elif game[1][i] == 0 and (game[2][i]!=0 or game[3][i]!=0):
            return True
        elif game[2][i] == 0 and game[3][i]!=0:
            return True
        elif game[0][i] == game[1][i] or game[1][i] == game[2][i] or game[2][i] == game[3][i] :
            return True
    return False
def canDown(game):
    for i in range(0,3):
        if game[3][i] == 0 and (game[2][i]!=0 or game[1][i]!=0 or game[0][i]!=0):
            return True
        elif game[2][i] == 0 and (game[1][i]!=0 or game[0][i]!=0):
            return True
        elif game[1][i] == 0 and game[0][i]!=0:
            return True
        elif game[0][i] == game[1][i] or game[1][i] == game[2][i] or game[2][i] == game[3][i] :
            return True
    return False

def canDown4(game):
    i = 3
    if game[3][i] == 0 and (game[2][i]!=0 or game[1][i]!=0 or game[0][i]!=0):
        return True
    elif game[2][i] == 0 and (game[1][i]!=0 or game[0][i]!=0):
        return True
    elif game[1][i] == 0 and game[0][i]!=0:
        return True
    elif game[0][i] == game[1][i] or game[1][i] == game[2][i] or game[2][i] == game[3][i] :
        return True
    return False
count = [1]
def auto(game):
    count[0]+=1
    print count[0]

    for i in range(len(game)):
        print "[",
        for j in game[i]:
            if j<10:
                print "   ",
            elif j< 100:
                print "  ",
            elif j<1000:
                print " ",
            print j,
        print "]"
    print "------------------------------"
    if canDown4(game):
        auto(add_two(down(game)[0]))
    elif canRight(game):
        auto(add_two(right(game)[0]))
    elif canDown(game):
        auto(add_two(down(game)[0]))
    elif canUp(game):
        auto(add_two(up(game)[0]))

    elif canLeft(game):
        auto(add_two(left(game)[0]))

game = new_game(4)

auto(add_two(game))

