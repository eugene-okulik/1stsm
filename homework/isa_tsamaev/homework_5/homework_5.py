person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person


text1 = "результат операции: 42"
text2 = "результат операции: 514"
text3 = "результат работы программы: 9"

index_text1 = text1.index(':')
int_text1 = int(text1[index_text1 + 2:])

index_text2 = text2.index(':')
int_text2 = int(text2[index_text2 + 2:])

index_text3 = text3.index(':')
int_text3 = int(text3[index_text3 + 2:])

print(int_text1 + 10, int_text2 + 10, int_text3 + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
