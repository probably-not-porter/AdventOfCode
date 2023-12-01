sum=0;
while read -r line; do 
    echo "Line: $line" 
    nums=$( echo $line | sed 's/[^0-9]*//g'); 
    sum=$((sum + ${nums:0:1}${nums:0-1})); 
    echo "Line Value: ${nums:0:1}${nums:0-1}"
    echo ""
    done < input.txt
echo "TOTAL SCORE: $sum";
# Answer is 54634