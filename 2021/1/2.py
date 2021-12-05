arr = []
for line in open('input'):
    measurement = int(line[:-1])
    arr.append(measurement)

increases = 0
for i in range(1, len(arr)-1):
    currentWindow = arr[i] + (arr[i+1] if i+1 < len(arr) else 0) + (arr[i+2] if i+2 < len(arr) else 0)
    nextWindow = arr[i+1] + (arr[i+2] if i+2 < len(arr) else 0) + (arr[i+3] if i+3 < len(arr) else 0)

    print(currentWindow, nextWindow)

    if nextWindow > currentWindow:
        increases = increases + 1
print(increases)
