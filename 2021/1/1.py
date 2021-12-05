previous = -9999999999
increases = -1 # first measurement doesn't count
for line in open('input'):
    measurement = int(line[:-1])
    print(measurement  )
    if measurement > previous:
        increases = increases+1
    previous = measurement
print(increases)
