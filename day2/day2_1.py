with open('input.txt') as f:
    lines = f.readlines()
    posx = 0
    posy = 0
    for line in lines:
        line = line.replace("\n","").split(" ")
        if line[0] == "up":
            posy = posy - int(line[1])
        elif line[0] == "down":
            posy = posy + int(line[1])
        elif line[0] == "forward":
            posx = posx + int(line[1])
        else:
            print("ERROR")
    print(str(posy) + " depth")
    print(str(posx) + " h pos")
    print("depth x h pos = " + str(posx * posy))
        