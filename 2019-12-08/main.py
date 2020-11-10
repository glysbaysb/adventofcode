#!/bin/env python3

WIDTH = 25
HEIGHT = 6

LAYER_LENGTH = WIDTH * HEIGHT

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

for line in open('input'):
    allChunks = list(chunkstring(line, LAYER_LENGTH))
    layers = []
    for chunk in allChunks:
        if chunk == '\n':
            continue
        layers.insert(len(layers) - 1, list(chunk))
for h in range(HEIGHT):
    for w in range(WIDTH):
        for l in range(len(layers)):
            if layers[l][h * WIDTH + w] == '2':
                continue
            # white output on black terminal so invert
            if layers[l][h*WIDTH + w] == '0':
                print(' ', end='')
            else:
                print('#', end='')
            break
    print()
