import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_13_data_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


with open(hw_13_data_path, encoding="utf-8") as task_data:
    for line in task_data:
        parts = line.split(" - ")
        date_parts = parts[0].split(". ")
        file_date = datetime.datetime.strptime(date_parts[1], "%Y-%m-%d %H:%M:%S.%f")
        if date_parts[0] == "1":
            plus_one_week = file_date + datetime.timedelta(weeks=1)
            print(plus_one_week)
        elif date_parts[0] == "2":
            week_day = file_date.strftime("%A")
            print(week_day)
        elif date_parts[0] == "3":
            date_difference = datetime.datetime.now() - file_date
            print(date_difference.days)
