with open('input.txt') as f:
    lines = f.readlines()
    prev_line = None
    stats = [0,0,0,0]
    for line in lines:
        line_n = int(line.replace("\n", ""))
        print(str(line_n))
        if prev_line == None:
            stats[0] = stats[0] + 1
        elif prev_line == line_n:
            stats[1] = stats[1] + 1
        elif prev_line > line_n:
            stats[2] = stats[2] + 1
        else:
            stats[3] = stats[3] + 1

        prev_line = line_n

    print("No previous data: " + str(stats[0]))
    print("No change: " + str(stats[1]))
    print("decreased: " + str(stats[2]))
    print("increased: " + str(stats[3]))