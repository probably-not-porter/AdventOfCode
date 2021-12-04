with open('input.txt') as f:
    lines = f.readlines()
    prev_lines = [0,int(lines[0].replace("\n", "")),int(lines[1].replace("\n", ""))]
    prev_set = None
    stats = [0,0,0,0]
    for x in range(2,len(lines)):
        line = lines[x]
        line_n = int(line.replace("\n", ""))
        prev_lines.append(line_n)
        prev_lines.pop(0)
        
        set_n = prev_lines[0] + prev_lines[1] + prev_lines[2]
        if prev_set == None:
            stats[0] = stats[0] + 1
            print(str(line_n) + " x")
        elif prev_set == set_n:
            stats[1] = stats[1] + 1
            print(str(line_n) + " =")
        elif prev_set > set_n:
            stats[2] = stats[2] + 1
            print(str(line_n) + " >")
        else:
            stats[3] = stats[3] + 1
            print(str(line_n) + " <")


        
        prev_set = set_n

    print("No previous data: " + str(stats[0]))
    print("No change: " + str(stats[1]))
    print("decreased: " + str(stats[2]))
    print("increased: " + str(stats[3]))