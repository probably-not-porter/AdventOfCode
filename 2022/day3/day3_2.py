def main():
    with open('input.txt') as f:
        lines = f.readlines()
    f.close()
    total = 0
    for x in range(0,len(lines),3):
        first = lines[x].replace("\n",'').replace(" ","")
        second = lines[x+1].replace("\n",'').replace(" ","")
        third = lines[x+2].replace("\n",'').replace(" ","")
        for ch in first:
            if ch in second and ch in third:
                val = ord(ch) - 64
                if ch.isupper(): val = val + 26
                else: val = val - 32
                total += val
                break
    print("The sum of the badge priorities is: " + str(total))
main()
# Answer is 2444