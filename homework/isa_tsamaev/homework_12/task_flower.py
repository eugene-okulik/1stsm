class Flower:
    def __init__(self, color, freshness, stem_length, lifetime, price):
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.lifetime = lifetime
        self.price = price

    def __repr__(self):
        freshness = "свежий" if self.freshness else "несвежий"
        return (
            f"{self.__class__.__name__}("
            f"Цвет - {self.color}, "
            f"{freshness}, "
            f"стебель - {self.stem_length} см., "
            f"срок жизни - {self.lifetime} д., "
            f"цена - {self.price} р.)"
        )

    def __str__(self):
        freshness = "свежий" if self.freshness else "несвежий"
        return (
            f"{self.__class__.__name__}("
            f"Цвет - {self.color}, "
            f"{freshness}, "
            f"стебель - {self.stem_length} см., "
            f"срок жизни - {self.lifetime} д., "
            f"цена - {self.price} р.)"
        )


class Rose(Flower):
    pass


class Lily(Flower):
    pass


class Tulip(Flower):
    pass


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_price(self):
        return f"Стоимость букета: {sum(flower.price for flower in self.flowers)} р."

    def get_avg_lifetime(self):
        return f"Срок жизни букета: {round(sum(flower.lifetime for flower in self.flowers) / len(self.flowers))} д."

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness, reverse=True)
        result = "\n".join(map(str, self.flowers))
        return f"Сортировка по свежести цветов:\n{result}"

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)
        result = "\n".join(map(str, self.flowers))
        return f"Сортировка по цвету:\n{result}"

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)
        result = "\n".join(map(str, self.flowers))
        return f"Сортировка по длине стебля:\n{result}"

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)
        result = "\n".join(map(str, self.flowers))
        return f"Сортировка по цене:\n{result}"

    def search_by_color(self):
        input_color = input("Введите цвет: ")
        result = list(filter(
            lambda flower: flower.color.lower() == input_color.lower(),
            self.flowers
        ))
        flowers_result = "\n".join(map(str, result))
        return (
            f"Цветы соответствующего цвета:\n{flowers_result}"
            if result
            else "Совпадений по цвету нет"
        )


rose_1 = Rose("Red", True, 45, 10, 100)
rose_2 = Rose("Pink", True, 70, 8, 150)
lily_1 = Lily("Blue", True, 50, 7, 120)
lily_2 = Lily("White", True, 60, 6, 120)
tulip_1 = Tulip("Purple", True, 40, 10, 145)
tulip_2 = Tulip("Pink", False, 50, 4, 140)

flowers = [rose_1, rose_2, lily_1, lily_2, tulip_1, tulip_2]

bouquet = Bouquet(flowers)
print(bouquet.get_price())
print(bouquet.get_avg_lifetime())
print(bouquet.sort_by_color())
print(bouquet.sort_by_price())
print(bouquet.sort_by_stem_length())
print(bouquet.sort_by_freshness())
print(bouquet.search_by_color())
