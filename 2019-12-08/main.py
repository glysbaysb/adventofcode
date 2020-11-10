#!/bin/env python3

WIDTH = 25
HEIGHT = 6

LAYER_LENGTH = WIDTH * HEIGHT

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

found0 = 9999
foundChunk = ''

for line in open('input'):
    allChunks = list(chunkstring(line, LAYER_LENGTH))
    for chunk in allChunks:
        if chunk == '\n':
            continue
        if chunk.count('0') < found0:
            found0 = chunk.count('0')
            foundChunk = chunk
print(foundChunk)
print(foundChunk.count('1') * foundChunk.count('2'))
