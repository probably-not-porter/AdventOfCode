def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()
    score = 0
    score_matrix = {
        "A":{"X":3, "Y":4, "Z":8},
        "B":{"X":1, "Y":5, "Z":9},
        "C":{"X":2, "Y":6, "Z":7}
    }

    for line in lines:
        round = line.replace("\n",'').split(' ')
        score += score_matrix[round[0]][round[1]]
    print("Total Score from all rounds is (Second Matrix): " + str(score))
main()
# Answer is 11258