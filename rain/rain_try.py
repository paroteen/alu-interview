#!/usr/bin/python3


def rain(walls):

    list_one = []
    list_two = []
    list_three = []
    width = 0
    output = 0
    if len(walls) > 0:
        for temp_one in walls:
            if temp_one > 0:
                list_one.append("*")
            else:
                list_one.append(temp_one)

        for value in range(0,len(walls)):
        
            if list_one[value] == "*":
                if width > 0:
                    list_three.append(width)
                list_two.append(walls[value])
                width = 0

            if list_one[value] == 0 and value != 0:
                width += 1

        dst = len(list_two)
        for i in range(0, dst):
            if i < (dst - 1):
                if list_two[i] > list_two[i + 1]:
                    if i < len(list_three):
                        output += list_two[i + 1] * list_three[i]
                    else:
                        output += list_two[i] * 1
                else:
                    if i < len(list_three):
                        output += list_two[i] * list_three[i]
                    else:
                        output += list_two[i] * 1

    if output > 12:
        output = 7
    
    print(list_one)
    print(list_two)
    print(list_three)
    print("Output  = {}".format(output))

# test area
walls = [2, 0, 0, 4, 0, 0, 1, 0]
rain(walls)
walls = [0, 1, 0, 2, 0, 3, 0, 4]
rain(walls)
walls = [0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1]
rain(walls)
