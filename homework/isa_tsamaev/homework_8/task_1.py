import random

salary = int(input("Введите зарплату: "))
bonus = random.choice([True, False])

if bonus:
    salary += random.randrange(1, 10000)

print(f"{salary}, {bonus} - '${salary}'")
