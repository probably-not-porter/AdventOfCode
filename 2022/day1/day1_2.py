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
    totals_list.sort()
    top_3 = totals_list[-3:]
    print("Max Calorie Load (Top 3) is: " + str(sum(top_3)) + " cal")
main()
# Answer is 201524