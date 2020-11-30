def paper(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def ribbon(l, w, h):
    smallest = min(l, w, h)
    if smallest ==  l:
        secondSmallest = min(w, h)
    elif smallest == w:
        secondSmallest = min(l, h)
    else:
        secondSmallest = min(l, w)
    return (2*smallest + 2*secondSmallest) + (l * w * h)

print(ribbon(2, 3, 4))
print(ribbon(1, 1, 10))

totalLength = 0
for line in open('input'):
    l, w, h = line.split('x')
    totalLength = totalLength + ribbon(int(l), int(w), int(h))
print(totalLength)

