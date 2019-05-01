from random import randint
from main_classes import *


def dice():
    x = randint(1, 6)
    return x


def main():
    s1 = Snake(start=10, stop=2)
    s2 = Snake(start=40, stop=2)
    s3 = Snake(start=99, stop=1)
    # Initializing three ladders and three snakes p.s more can be added if you want
    l1 = Ladder(start=5, stop=20)
    l2 = Ladder(start=27, stop=83)
    l3 = Ladder(start=47, stop=100)
    n = int(input("enter the number of players"))
    print("enter the name of each players")
    if n == 2:
        name1 = input()
        name2 = input()
        p1 = Player(pos=0, name=name1)
        p2 = Player(pos=0, name=name2)
    if n == 3:
        name1 = input()
        name2 = input()
        name3 = input()
        p1 = Player(pos=0, name=name1)
        p2 = Player(pos=0, name=name2)
        p3 = Player(pos=0, name=name3)
    if n == 4:
        name1 = input()
        name2 = input()
        name3 = input()
        name4 = input()
        p1 = Player(pos=0, name=name1)
        p2 = Player(pos=0, name=name2)
        p3 = Player(pos=0, name=name3)
        p4 = Player(pos=0, name=name4)

    # for 2 players

    if n == 2:
        while p1.pos != 100 and p2.pos != 100:
            for x in range(1, 3):
                print("Player" + " " + str(x) + " " + "roll dice")
                a = input("press y to roll the dice")
                print()
                if a == "y":
                    no = dice()
                    print("the dice rolled"+" " + str(no))
                else:
                    print("hit the correct key you miss a chance *_*")
                    continue
                if x == 1 and p1.pos + no < 101:
                    p1.pos += no
                    if p1.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p1.pos = s1.stop
                    elif p1.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p1.pos = s2.stop
                    elif p1.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p1.pos = s3.stop
                    if p1.pos == l1.start:
                        print("you reached a ladder advance (;")
                        print()
                        p1.pos = l1.stop
                    elif p1.pos == l2.start:
                        print("you reached a ladder advance (;")
                        print()
                        p1.pos = l2.stop
                    elif p1.pos == l3.start:
                        print("you reached a ladder advance (;")
                        print()
                        p1.pos = l3.stop

                    print("now player 1 is in position" + " " + str(p1.pos))
                    print()
                elif x == 2 and p2.pos + no < 101:
                    p2.pos += no
                    if p2.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p2.pos = s1.stop
                    elif p2.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p2.pos = s2.stop
                    elif p2.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p2.pos = s3.stop
                    elif p2.pos == l1.start:
                        print("you reached a ladder advance (;")
                        print()
                        p2.pos = l1.stop
                    elif p2.pos == l2.start:
                        print("you reached a ladder advance (;")
                        print()
                        p2.pos = l2.stop
                    elif p2.pos == l3.start:
                        print("you reached a ladder advance (;")
                        print()
                        p2.pos = l3.stop
                    print("now player 2 is in position" + " " + str(p2.pos))
                    print()
        if p1.pos == 100:
            print("Player 1 " + " " + p1.name + " " + "is the winner")
        elif p2.pos == 100:
            print("Player 2 " + " " + p2.name + " " + "is the winner")

    # for 3 players

    elif n == 3:
        while p1.pos != 100 and p2.pos != 100 and p3.pos != 100:
            for x in range(1, 4):
                print("Player" + " " + str(x) + " " + "roll dice")
                a = input("press y to roll the dice")
                if a == "y":
                    no = dice()
                    print("the dice rolled" + " " + str(no))
                else:
                    print("hit the correct key you miss a chance *_*")
                    continue
                if x == 1 and p1.pos + no < 101:
                    p1.pos += no
                    if p1.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        p1.pos = s1.stop
                    elif p1.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        p1.pos = s2.stop
                    elif p1.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        p1.pos = s3.stop
                    if p1.pos == l1.start:
                        print("you reached a ladder advance (;")
                        p1.pos = l1.stop
                    elif p1.pos == l2.start:
                        print("you reached a ladder advance (;")
                        p1.pos = l2.stop
                    elif p1.pos == l3.start:
                        print("you reached a ladder advance (;")
                        p1.pos = l3.stop

                    print("now player 1 is in position" + " " + str(p1.pos))
                    print()
                elif x == 2 and p2.pos + no < 101:
                    p2.pos += no
                    if p2.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        p2.pos = s1.stop
                    elif p2.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        p2.pos = s2.stop
                    elif p2.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        p2.pos = s3.stop
                    if p2.pos == l1.start:
                        print("you reached a ladder advance (;")
                        p2.pos = l1.stop
                    elif p2.pos == l2.start:
                        print("you reached a ladder advance (;")
                        p2.pos = l2.stop
                    elif p2.pos == l3.start:
                        print("you reached a ladder advance (;")
                        p2.pos = l3.stop

                    print("now player 2 is in position" + " " + str(p2.pos))
                elif x == 3 and p3.pos + no < 101:
                    p2.pos += no
                    if p3.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        p3.pos = s1.stop
                    elif p3.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        p3.pos = s2.stop
                    elif p3.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        p3.pos = s3.stop
                    if p3.pos == l1.start:
                        print("you reached a ladder advance (;")
                        p3.pos = l1.stop
                    elif p3.pos == l2.start:
                        print("you reached a ladder advance (;")
                        p3.pos = l2.stop
                    elif p3.pos == l3.start:
                        print("you reached a ladder advance (;")
                        p3.pos = l3.stop

                    print("now player 3 is in position" + " " + str(p3.pos))
        if p1.pos == 100:
            print("Player 1 " + " " + p1.name + " " + "is the winner")
        elif p2.pos == 100:
            print("Player 2 " + " " + p1.name + " " + "is the winner")
        elif p3.pos == 100:
            print("Player 3 " + " " + p1.name + " " + "is the winner")

    # for 4 players
    elif n == 4:
        while p1.pos != 100 and p2.pos != 100 and p3.pos != 100 and p4.pos != 100:
            for x in range(1, 3):
                print("Player" + " " + str(x) + " " + "roll dice")
                a = input("press y to roll the dice")
                print()
                if a == "y":
                    no = dice()
                    print("the dice rolled" + " " + str(no))
                else:
                    print("hit the correct key you miss a chance *_*")
                    continue
                if x == 1 and p1.pos + no < 101:
                    p1.pos += no
                    if p1.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p1.pos = s1.stop
                    elif p1.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p1.pos = s2.stop
                    elif p1.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p1.pos = s3.stop
                    if p1.pos == l1.start:
                        print("you reached a ladder advance (;")
                        print()
                        p1.pos = l1.stop
                    elif p1.pos == l2.start:
                        print("you reached a ladder advance (;")
                        print()
                        p1.pos = l2.stop
                    elif p1.pos == l3.start:
                        print("you reached a ladder advance (;")
                        print()
                        p1.pos = l3.stop

                    print("now player 1 is in position" + " " + str(p1.pos))
                    print()
                elif x == 2 and p2.pos + no < 101:
                    p2.pos += no
                    if p2.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p2.pos = s1.stop
                    elif p2.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p2.pos = s2.stop
                    elif p2.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p2.pos = s3.stop
                    if p2.pos == l1.start:
                        print("you reached a ladder advance (;")
                        print()
                        p2.pos = l1.stop
                    elif p2.pos == l2.start:
                        print("you reached a ladder advance (;")
                        print()
                        p2.pos = l2.stop
                    elif p2.pos == l3.start:
                        print("you reached a ladder advance (;")
                        print()
                        p2.pos = l3.stop

                    print("now player 2 is in position" + " " + str(p2.pos))
                    print()
                elif x == 3 and p3.pos + no < 101:
                    p3.pos += no
                    if p3.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p3.pos = s1.stop
                    elif p3.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p3.pos = s2.stop
                    elif p3.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p3.pos = s3.stop
                    if p3.pos == l1.start:
                        print("you reached a ladder advance (;")
                        print()
                        p3.pos = l1.stop
                    elif p3.pos == l2.start:
                        print("you reached a ladder advance (;")
                        print()
                        p3.pos = l2.stop
                    elif p3.pos == l3.start:
                        print("you reached a ladder advance (;")
                        print()
                        p3.pos = l3.stop

                    print("now player 3 is in position" + " " + str(p3.pos))
                    print()
                elif x == 4 and p4.pos + no < 101:
                    p4.pos += no
                    if p4.pos == s1.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p4.pos = s1.stop
                    elif p4.pos == s2.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p4.pos = s2.stop
                    elif p4.pos == s3.start:
                        print("you encountered a snake *.* go down")
                        print()
                        p4.pos = s3.stop
                    if p4.pos == l1.start:
                        print("you reached a ladder advance (;")
                        print()
                        p4.pos = l1.stop
                    elif p4.pos == l2.start:
                        print("you reached a ladder advance (;")
                        print()
                        p4.pos = l2.stop
                    elif p4.pos == l3.start:
                        print("you reached a ladder advance (;")
                        print()
                        p4.pos = l3.stop

                    print("now player 4 is in position" + " " + str(p4.pos))
                    print()
        if p1.pos == 100:
            print("Player 1 " + " " + p1.name + " " + "is the winner")
        elif p2.pos == 100:
            print("Player 2 " + " " + p1.name + " " + "is the winner")
        elif p3.pos == 100:
            print("Player 3 " + " " + p1.name + " " + "is the winner")
        elif p4.pos == 100:
            print("Player 4 " + " " + p1.name + " " + "is the winner")


main()
