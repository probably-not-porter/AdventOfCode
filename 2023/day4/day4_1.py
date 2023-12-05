def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()
    TOTAL_SCORE = 0
    for line in lines:
        cardID, cardString = line.split(":")
        cardNums, winningNums = [x.split() for x in cardString.split("|")]
        cardID = int(cardID.replace("Card ", ""))
        cardNums = [eval(i) for i in cardNums]
        winningNums = [eval(i) for i in winningNums]
        score = 0

        for num in cardNums:
            if num in winningNums:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
        TOTAL_SCORE += score
        print("===== CARD #" + str(cardID) + " =====")
        print("cardNums", cardNums)
        print("winningNums", winningNums)
        print("Score", score)
        print("")
    print("TOTAL SCORE", TOTAL_SCORE)

main()
# Answer is 27845