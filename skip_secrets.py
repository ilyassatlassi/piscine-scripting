import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    file_name = sys.argv[1]

    if not os.path.isfile(file_name) or not os.access(file_name, os.R_OK):
        sys.exit(1)

    try:
        filtered_lines = []
        with open(file_name, 'r') as input_file:
            for line in input_file:
                if "pineapple" not in line:
                    filtered_lines.append(line)

        with open("out.txt", "w") as output_file:
            output_file.writelines(filtered_lines)

    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()
