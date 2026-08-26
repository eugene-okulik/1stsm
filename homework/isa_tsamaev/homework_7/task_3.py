text1 = "результат операции: 42"
text2 = "результат операции: 54"
text3 = "результат работы программы: 209"
text4 = "результат: 2"


def add_ten(*args):
    result = []

    for text in args:
        num = text.split()
        result.append(int(num[-1]) + 10)

    return result


processed_results = add_ten(text1, text2, text3, text4)

print(*processed_results, sep='\n')
