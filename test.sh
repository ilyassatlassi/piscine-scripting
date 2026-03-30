#!/usr/bin/env bash

set -e

IMAGE="ghcr.io/01-edu/imperative-piscine-sh:latest"


if [ -z "$1" ]; then
    echo "Usage: ./test.sh <exercise>"
    exit 1
fi

EXERCISE="$1"
EXERCISE="${EXERCISE%.sh}"

echo "Testing: $EXERCISE"

mkdir -p student
cp "$EXERCISE.sh" student/ 2>/dev/null || true

docker run --rm \
    -v "$PWD/student:/tmp/student:z" \
    -e EXERCISE="$EXERCISE" \
    -w /tmp \
    "$IMAGE"

rm -rf student
