import math

with open('input') as file:
    lines = file.read().split("\n")
    timestamp = int(lines[0])
    buses = list(filter(lambda x: x != 'x', lines[1].split(',')))

    nextBusTimestamp = math.inf
    nextBusId = None

    for bus in buses:
        nextDeparture = math.ceil(timestamp / int(bus)) * int(bus)
        if nextBusTimestamp > nextDeparture:
            nextBusTimestamp = nextDeparture
            nextBusId = int(bus)
    print(timestamp, nextBusTimestamp, nextBusId)
    print(nextBusId * (nextBusTimestamp - timestamp))
