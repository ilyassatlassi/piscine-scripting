if [[ $# -ne 2 ]]; then
    echo "Error: expect 2 arguments" >&2
    exit 1
fi

if [[ $1 != "-e" ]] && [[ $1 != "-i" ]]; then
    echo "Error: unknown flag" >&2
    exit 1
fi

case $1 in
    "-e")
        if [[ -n $(getent passwd $2) ]]; then
            echo "yes"
        else
            echo "no"
        fi
        ;;
    "-i")
        getent passwd $2
        ;;
esac
