
if [[ $# -ne 1 ]]; then
    >&2 echo "Error: expect 1 argument only!"
    exit 1
fi

num_students=$1
declare -a names
declare -a grades

for (( i=1; i<=num_students; i++ ))
do
    read -p "Student Name #$i: " current_name
    names+=("$current_name")

    read -p "Student Grade #$i: " current_grade
    
    if [[ ! "$current_grade" =~ ^[0-9]+$ ]] || [[ "$current_grade" -gt 100 ]]; then
        >&2 echo "Error: The grade '$current_grade' is not a valid input. Only numerical grades between 0 and 100 are accepted."
        exit 1
    fi
    
    grades+=("$current_grade")
done

for (( i=0; i<num_students; i++ ))
do
    name=${names[$i]}
    grade=${grades[$i]}

    if [[ "$grade" -ge 90 ]]; then
        echo "$name: You did an excellent job!"
    elif [[ "$grade" -ge 70 ]]; then
        echo "$name: You did a good job!"
    elif [[ "$grade" -ge 50 ]]; then
        echo "$name: You need a bit more effort!"
    else
        echo "$name: You had a poor performance!"
    fi
done
