#!/bin/bash
setopt shwordsplit

sum=0;
linenum=0;
while read -r line; do 
    ((linenum++))
    echo "LINENUM: $linenum"
    
    value=${line#*|}

    for one_thing in $value; do
        if test ${#one_thing} == 2; then
            ((sum++))
            echo "   (one)   STRING: $one_thing, CURRENT SUM: $sum"
        fi
        if test ${#one_thing} == 4; then
            ((sum++))
            echo "   (four)  STRING: $one_thing, CURRENT SUM: $sum"
        fi
        if test ${#one_thing} == 3; then
            ((sum++))
            echo "   (seven) STRING: $one_thing, CURRENT SUM: $sum"
        fi
        if test ${#one_thing} == 7; then
            ((sum++))
            echo "   (eight) STRING: $one_thing, CURRENT SUM: $sum"
        fi
        echo "        STRING: $one_thing, CURRENT SUM: $sum"
    done

done < input.txt;

echo ""
echo "TOTAL SCORE: $sum";
# Answer is 369