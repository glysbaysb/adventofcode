#!/bin/env python3

def get_max_positions(movments):
    maxX = 0
    minX = 0
    curX = 0

    maxY = 0
    minY = 0
    curY = 0

    for m in movments:
        direction = m[0]
        length = int(m[1:])

        # move
        if direction == 'L':
            curX -= length
        elif direction == 'R':
            curX += length
        elif direction == 'U':
            curY += length
        elif direction == 'D':
            curY -= length

        # check bounds
        if maxX < curX:
            maxX = curX
        if minX > curX:
            minX = curX
        if maxY < curY:
            maxY = curY
        if minY > curY:
            minY = curY


    return maxX - minY, maxY - minY


'''
l1 = ['R8','U5','L5','D3']
l2 = ['U7','R6','D4','L4']
print(get_max_positions(l1))
print(get_max_positions(l2))
'''
f = open('input')
l1 = f.readline().split(',')
l2 = f.readline().split(',')

print(get_max_positions(l1), get_max_positions(l2))
