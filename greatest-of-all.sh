 
max=0

for i in {1..10}
do
	read -p "Enter a number: " current_num

	if [[ ! $current_num =~ ^[0-9]+$ ]]; then
		echo "ERROR: Invalid input only positive numerical characters are allowed"
		exit 1
	fi

	if [[ $current_num -gt 1000 ]]; then
		echo "ERROR: The number entered is too large"
		exit 1
	fi

	if [[ "$current_num" -gt "$max" ]]; then
        max=$current_num
    fi
done

echo "The largest number is: $max"
