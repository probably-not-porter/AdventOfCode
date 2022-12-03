def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()
    score = 0
    score_matrix = {
        "A":{"X":4, "Y":8, "Z":3},
        "B":{"X":1, "Y":5, "Z":9},
        "C":{"X":7, "Y":2, "Z":6}
    }

    for line in lines:
        round = line.replace("\n",'').split(' ')
        score += score_matrix[round[0]][round[1]]
    print("Total Score from all rounds is: " + str(score))
main()
# Answer is 14531