#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo "Error: two numbers must be provided"
elif [[ ! $1 =~ ^-?[0-9]+$ ]] || [[ ! $2 =~ ^-?[0-9]+$ ]]; then
    echo "Error: both arguments must be integers"
elif [[ $2 -eq 0 ]]; then
    echo "Error: division by zero is not allowed"
else
    echo "$1 / $2" | bc
fi
