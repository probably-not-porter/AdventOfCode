def main(sim_length):
    with open('day6_input.txt') as f:
        inp_school = f.read().replace('\n', "").split(",")
    f.close()

    school = {
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
        "1": 0,
        "0": 0,
        "-1": 0,
    }
    # set up
    for inp in inp_school:
        school[inp] = school[inp] + 1
    
    # simulate with N(sim_length) time
    for day in range(sim_length):
        _8 = school["8"]
        _7 = school["7"]
        _6 = school["6"]
        _5 = school["5"]
        _4 = school["4"]
        _3 = school["3"]
        _2 = school["2"]
        _1 = school["1"]
        _0 = school["0"]

        school["0"] = _1
        school['1'] = _2
        school["2"] = _3
        school["3"] = _4
        school["4"] = _5
        school["5"] = _6
        school["6"] = _7 + _0
        school["7"] = _8
        school["8"] = _0

    print(school["8"] + school["7"] + school["6"] + school["5"] + school["4"] + school["3"] + school["2"] + school["1"] + school["0"] )

# Part 1
main(80)
# Answer is 396210

# Part 2
main(256)
# Answer is 1770823541496