def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()
    total = 0
    for line in lines:
        bag = line.replace("\n",'').replace(" ","")
        pocketA, pocketB = bag[:len(bag)//2], bag[len(bag)//2:]
        for ch in pocketA:
            if ch in pocketB:
                val = ord(ch) - 64
                if ch.isupper(): val = val + 26
                else: val = val - 32
                total += val
                break
    print("The sum of the priorities is: " + str(total))
main()
# Answer is 7817