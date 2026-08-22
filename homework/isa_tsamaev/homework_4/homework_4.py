my_dict = {
    "tuple": (1, 2, 3, 4, 5, "text"),
    "list": [10, 20, 30, 40, 50, "word"],
    "dict": {
        "fruit": "apple",
        "quantity": 10,
        "price": 25.5,
        "available": True,
        "category": "food",
    },
    "set": {100, 200, 300, 400, 500}
}


my_dict["list"].append(60)
my_dict["list"].pop(1)

my_dict["dict"][("i am a tuple",)] = False
del my_dict["dict"]["category"]

my_dict["set"].add("num")
my_dict["set"].remove(400)

print(my_dict["tuple"][-1])
print(my_dict)
