def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()

    copies = [1] * len(lines)

    for line in lines:
        cardID, cardString = line.split(":")
        cardNums, winningNums = [x.split() for x in cardString.split("|")]
        cardID = int(cardID.replace("Card ", ""))
        cardNums = [eval(i) for i in cardNums]
        winningNums = [eval(i) for i in winningNums]
        score = 0

        for num in cardNums:
            if num in winningNums:
                score += 1
        for x in range(1, score + 1):
            copies[cardID - 1 + x] += copies[cardID - 1]

        print("===== CARD #" + str(cardID) + " =====")
        print("cardNums", cardNums)
        print("winningNums", winningNums)
        print("copies", copies[cardID - 1])
        print("")
    print("TOTAL", str(sum(copies)))
main()
# Answer is 9496801