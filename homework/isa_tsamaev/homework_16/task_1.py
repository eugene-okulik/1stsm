import csv
import os

import dotenv
import mysql.connector as mysql

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_path = os.path.join(
    homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)

db_query = '''
    SELECT gr.title as group_title,
        b.title as book_title,
        sub.title as subject_title,
        les.title as lesson_title,
        mar.value as mark_value
    FROM subjects sub
    JOIN lessons les ON sub.id = les.subject_id
    JOIN marks mar ON les.id = mar.lesson_id
    JOIN students stud ON mar.student_id = stud.id
    JOIN `groups` gr ON stud.group_id = gr.id
    JOIN books b on stud.id = b.taken_by_student_id
    WHERE stud.name = %s
        AND stud.second_name = %s
        AND gr.title = %s
        AND b.title = %s
        AND sub.title = %s
        AND les.title = %s
        AND mar.value = %s
'''
try:
    cursor = db.cursor(dictionary=True)

    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            select_values = (
                row['name'],
                row['second_name'],
                row['group_title'],
                row['book_title'],
                row['subject_title'],
                row['lesson_title'],
                row['mark_value']
            )

            cursor.execute(db_query, select_values)
            db_result = cursor.fetchall()

            if not db_result:
                print(row)
finally:
    db.close()
