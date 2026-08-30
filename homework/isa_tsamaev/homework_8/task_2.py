import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    a = 0
    b = 1

    while True:
        yield b
        a, b = b, a + b


count = 1
for number in fibonacci():
    if count in (5, 200, 1000, 100_000):
        print(number)

    if count == 100_000:
        break

    count += 1
