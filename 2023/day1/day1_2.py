def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()

    TTL = 0
    for line in lines:
        line_vals = []
        line_n = line.replace("\n", "")
        print("Line: " + str(line_n))

        for c in range(len(line_n)):
            if line[c].isdigit():
                line_vals.append(line[c])

            printNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

            for x in printNums:
                if line[c:c+len(x)] == x:
                    line_vals.append(printNums.index(x) + 1)

        print("Line Value: " + (str(line_vals[0]) + str(line_vals[-1])))
        TTL += int(str(line_vals[0]) + str(line_vals[-1]))

    print("TOTAL: " + str(TTL))

main()
# Answer is 53855