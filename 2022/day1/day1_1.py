def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()
    current_total = 0
    totals_list = []
    for line in lines:
        line_n = line.replace("\n", "")
        if line_n.isdigit(): current_total = current_total + int(line_n)
        else:
            x = 0
            x = current_total
            totals_list.append(x)
            current_total = 0
    print("Max Calorie Load is: " + str(max(totals_list)) + " cal")
main()
# Answer is 69281