import os
import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd=os.getenv('DB_PASSWORD'),
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

create_student_query = '''
INSERT INTO students (name, second_name)
VALUES (%s, %s)
'''
cursor.execute(create_student_query, ('Dmitry', 'Sokolov'))
student_id = cursor.lastrowid

create_book_query = '''
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
'''
cursor.executemany(
    create_book_query, [
        ('Python Crash Course', student_id),
        ('Clean Code', student_id)
    ]
)

create_group_query = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
'''
cursor.execute(
    create_group_query, (
        'Python_Automation_2026_2', 'Sep 2026', 'Apr 2027'
    )
)
group_id = cursor.lastrowid

update_student_query = '''
UPDATE students s
SET group_id = %s
WHERE s.id = %s
'''
cursor.execute(update_student_query, (group_id, student_id))

create_subject_query = '''
INSERT INTO subjects (title)
VALUES (%s)
'''
cursor.execute(create_subject_query, ('Database Systems',))
db_systems_subject_id = cursor.lastrowid

cursor.execute(create_subject_query, ('Automated Testing',))
auto_test_subject_id = cursor.lastrowid

create_lesson_query = '''
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
'''
cursor.execute(
    create_lesson_query, (
        'SQL Queries and Joins',
        db_systems_subject_id
    )
)
db_lesson_1_id = cursor.lastrowid

cursor.execute(
    create_lesson_query, (
        'Database Relationships',
        db_systems_subject_id
    )
)
db_lesson_2_id = cursor.lastrowid

cursor.execute(
    create_lesson_query, (
        'Test Automation Basics',
        auto_test_subject_id
    )
)
auto_test_lesson_1_id = cursor.lastrowid
cursor.execute(
    create_lesson_query, (
        'API Testing with Python',
        auto_test_subject_id
    )
)
auto_test_lesson_2_id = cursor.lastrowid

create_mark_query = '''
INSERT INTO marks (student_id, lesson_id, value)
VALUES (%s, %s, %s)
'''
cursor.executemany(
    create_mark_query, [
        (student_id, db_lesson_1_id, '9'),
        (student_id, db_lesson_2_id, '8'),
        (student_id, auto_test_lesson_1_id, '10'),
        (student_id, auto_test_lesson_2_id, '9'),
    ]
)

db.commit()


student_marks_query = '''
SELECT m.value
FROM marks m
WHERE m.student_id = %s
'''
cursor.execute(student_marks_query, (student_id,))
marks_data = cursor.fetchall()

student_books_query = '''
SELECT b.title
FROM books b
WHERE b.taken_by_student_id = %s
'''
cursor.execute(student_books_query, (student_id,))
books_data = cursor.fetchall()

student_info_query = '''
SELECT gr.title as "Group",
b.title as "Books",
sub.title as "Subject",
les.title as "Lesson",
mar.value as "Marks"
FROM subjects sub
JOIN lessons les ON sub.id = les.subject_id
JOIN marks mar ON les.id = mar.lesson_id
JOIN students stud ON mar.student_id = stud.id
JOIN `groups` gr ON stud.group_id = gr.id
LEFT JOIN books b on stud.id = b.taken_by_student_id
WHERE stud.id = %s
'''
cursor.execute(student_info_query, (student_id,))
student_info_data = cursor.fetchall()

print(marks_data, books_data, student_info_data, sep='\n')

db.close()
