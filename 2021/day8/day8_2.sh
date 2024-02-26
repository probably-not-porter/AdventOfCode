setopt shwordsplit

sum=0;
linenum=0;

#    1111
#   2    3
#   2    3
#    4444
#   5    6
#   5    6
#    7777

while read -r line; do 
    ((linenum++))
    echo "LINENUM: $linenum"
    val1="one";
    val4="four";
    val7="seven";
    val8="eight";
    seg1="none";
    seg2="none";
    seg3="none";
    seg4="none";
    seg5="none";
    seg6="none";
    seg7="none";
    
    for one_thing in $line; do


        if test ${#one_thing} == 2; then
            ((sum++))
            echo "   (one)   STRING: $one_thing, CURRENT SUM: $sum"
            val1=$one_thing;
        fi
        if test ${#one_thing} == 4; then
            ((sum++))
            echo "   (four)  STRING: $one_thing, CURRENT SUM: $sum"
            val4=$one_thing;
        fi
        if test ${#one_thing} == 3; then
            ((sum++))
            echo "   (seven) STRING: $one_thing, CURRENT SUM: $sum"
            val7=$one_thing;
        fi
        if test ${#one_thing} == 7; then
            ((sum++))
            echo "   (eight) STRING: $one_thing, CURRENT SUM: $sum"
            val8=$one_thing;
        fi
        echo "        STRING: $one_thing, CURRENT SUM: $sum"
    done
    echo "$val1, $val4, $val7, $val8"

done < input.txt;

echo ""
echo "TOTAL SCORE: $sum";
# Answer is 369