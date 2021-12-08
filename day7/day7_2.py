
def main():
    with open('day7_input.txt') as f:
        crabs_in = f.read().split(",")
        crabs = [int(i.replace("\n","")) for i in crabs_in]
    f.close()

    min_crab, max_crab, scores = min(crabs), max(crabs), []
    for x in range(min_crab, max_crab + 1): scores.append(sum(list(map(lambda crab: sum([i for i in range(1, abs(crab - x) + 1)]), crabs))))
    print("Fuel Requirement is: " + str(min(scores)) + " units")

main()
# Answer is 96744904
