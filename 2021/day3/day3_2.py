def main():
    with open('day3_input.txt') as f:
        l = f.readlines()
    f.close()
    lines_ox = list(l)
    lines_co2 = list(l)
    x = 0
    while len(lines_ox) > 1:
        col = [int(line[x].replace("\n", "")) for line in lines_ox]
        col.append(1)
        target_dig = max(set(col), key=col.count)
        lines_ox = filter(lambda line: int(line[x]) == target_dig, lines_ox)
        x = x + 1
    x = 0
    while len(lines_co2) > 1:
        col = [int(line[x].replace("\n", "")) for line in lines_co2]
        target_dig = min(set(col), key=col.count)
        lines_co2 = filter(lambda line: int(line[x]) == target_dig, lines_co2)
        x = x + 1
    print("Oxygen: " + lines_ox[0].replace("\n", ""))
    print("Co2: " + lines_co2[0].replace("\n", ""))
    print("Ox Int: " + str(int(lines_ox[0].replace("\n", ""), 2)))
    print("Co2 Int: " + str(int(lines_co2[0].replace("\n", ""), 2)))
    print("Solution: " + str(int(lines_ox[0].replace("\n", ""), 2) * int(lines_co2[0].replace("\n", ""), 2)))

main()
# Answer is 4432698