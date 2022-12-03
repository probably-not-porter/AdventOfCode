def main():
    with open('day4_input.txt') as f:
        lines = f.read().split("\n")
    f.close()

    # read and format
    draws = lines[0].split(",")
    boards = []

    for x in range(1, len(lines), 6):
        board = []
        board.append(lines[x+1].split())
        board.append(lines[x+2].split())
        board.append(lines[x+3].split())
        board.append(lines[x+4].split())
        board.append(lines[x+5].split())
        boards.append(board)

    #simulate game
    score = bingo(draws, boards)
    print(score)

def bingo(d,b):
    for i in range(len(d)):
        draw = d[i]
        for j in range(len(b)):
            board = b[j]
            for k in range(len(board)):
                row = board[k]
                for l in range(len(row)):
                    if row[l] == draw:
                        b[j][k][l] = "X"
        win = check_win(b)
        if win != None:
            return check_score(win * int(draw))
    return None

def check_score(winboard):
    total = 0
    for row in winboard:
        for el in row:
            if el.isdecimal():
                total = total + int(el)
    return total


def check_win(b):
    for board in b:
        if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" and board[0][3] == "X" and board[0][4] == "X"):
            return board
        elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X" and board[1][4] == "X"):
            return board
        elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" and board[2][3] == "X" and board[2][4] == "X"):
            return board
        elif (board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X" and board[3][4] == "X"):
            return board
        elif (board[4][0] == "X" and board[4][1] == "X" and board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X"):
            return board
        elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" and board[3][0] == "X" and board[4][0] == "X"):
            return board
        elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X" and board[4][1] == "X"):
            return board
        elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X" and board[4][2] == "X"):
            return board
        elif (board[0][3] == "X" and board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X" and board[4][3] == "X"):
            return board
        elif (board[0][4] == "X" and board[1][4] == "X" and board[2][4] == "X" and board[3][4] == "X" and board[4][4] == "X"):
            return board
    return None

main()
# Answer is 49686