def main():
    with open('day3_input.txt') as f:
        lines = f.readlines()
    f.close()
    
    col_totals = [0,0,0,0,0,0,0,0,0,0,0,0]

    for line in lines:
        line = line.replace("\n","")
        for x in range(len(line)):
            col_totals[x] = col_totals[x] + int(line[x])

    gamma_assembly = ""
    epsilon_assembly = ""
    for x in col_totals:
        if x > len(lines) / 2:
            gamma_assembly += "1"
            epsilon_assembly += "0"
        else:
            gamma_assembly += "0"
            epsilon_assembly += "1"

    print("Gamma Binary: " + gamma_assembly)
    print("Epsilon Binary: " + epsilon_assembly)
    print("Gamma Int: " + str(int(gamma_assembly, 2)))
    print("Epsilon Int: " + str(int(epsilon_assembly, 2)))
    print("Power Consumption: " + str(int(gamma_assembly, 2) * int(epsilon_assembly, 2)))
        
main()
#Answer is 3374136