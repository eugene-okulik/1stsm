for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FuzzBuzz")
    elif x % 3 == 0:
        print("Fuzz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
