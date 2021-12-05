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
    print(number, len(boards))
    for board in range(0, len(boards)):
        for y in range(0, len(boards[board])):
            for x in range(0, len(boards[board][y])):
                if boards[board][y][x][0] == number:
                    boards[board][y][x] = (number, True)

    for board in boards:
        # after every set, check
        # first rows
        checkCol = True # skip column check if we removed the whole board
        for y in range(0, len(board)):
            foundTrue = 0
            for x in range(0, len(board[y])):
                if board[y][x][1]:
                    foundTrue = foundTrue + 1
            if foundTrue == 5:
                print("hooray row", unmarked(board) * number)
                boards.remove(board)
                checkCol = False
                break
        if not checkCol: # if board has been removed, no need to check columns
            continue
        # then columns
        for x in range(0, 5):
            foundTrue = 0
            for y in range(0, 5):
                if board[y][x][1]:
                    foundTrue = foundTrue + 1
            if foundTrue == 5:
                print("hooray col", unmarked(board) * number)
                boards.remove(board)
                break
