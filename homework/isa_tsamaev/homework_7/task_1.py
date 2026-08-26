num = 5

x = int(input("Угадайте цифру: "))
while True:
    if x != num:
        x = int(input("Попробуйте снова: "))
    else:
        print("Поздравляю! Вы угадали!")
        break
