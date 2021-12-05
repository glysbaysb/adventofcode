def unmarked(board):
    sum = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if not board[x][y][1]:
                sum = sum + board[x][y][0]
    return sum
# read boards
numbers = []
boards = []

board = -1
for line in open('input'):
    if len(numbers) == 0:
        numbers = [int(x) for x in line.split(',')]
        continue
    if len(line) == 1:
        boards.append([])
        board = board + 1
        continue
    boards[board].append([(int(x), False) for x in line.strip().replace("  ", ' ').split(' ')])
# set
for number in numbers:
    for board in range(0, len(boards)):
        for y in range(0, len(boards[board])):
            for x in range(0, len(boards[board][y])):
                if boards[board][y][x][0] == number:
                    boards[board][y][x] = (number, True)

        # after every set, check
        # first rows
        for y in range(0, len(boards[board])):
            foundTrue = 0
            for x in range(0, len(boards[board][y])):
                if boards[board][y][x][1]:
                    foundTrue = foundTrue + 1
            if foundTrue == 5:
                print("hooray row", unmarked(boards[board]) * number)
        # then columns
        for x in range(0, 5):
            foundTrue = 0
            for y in range(0, 5):
                if boards[board][y][x][1]:
                    foundTrue = foundTrue + 1
            if foundTrue == 5:
                print("hooray col", unmarked(boards[board]) * number)
