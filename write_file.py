import datetime as dt

def to_do(tasks):
    with open("output.txt", "w") as file:
        for task_date, description in tasks:
            formatted_date = task_date.strftime("%A %d %B %Y")
            line = f"{formatted_date}: {description}\n"
            file.write(line)
