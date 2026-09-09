first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))


def choose_operation(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        else:
            operation = "/"

        return func(first, second, operation)

    return wrapper


@choose_operation
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second


result = calc(first_number, second_number, None)
print(f"Результат: {result}")
