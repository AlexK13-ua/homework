        # 13.2 Корзина для покупок

class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        # Повертаємо назву та ціну у зручному форматі
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        # Виводимо ім'я та прізвище
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}  # Словник, де ключ - об'єкт Item, значення - кількість
        self.user = user

    def add_item(self, item, cnt):
        # Додаємо товар. Якщо такий ключ вже є, значення просто перепишеться
        self.products[item] = cnt

    def get_total(self):
        total = 0
        # Проходимо по словнику: item - це об'єкт класу Item, cnt - число
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        # Формуємо багаторядковий вивід
        items_list = ""
        for item, cnt in self.products.items():
            items_list += f"{item.name}: {cnt} pcs.\n"

        # Використовуємо rstrip() щоб прибрати зайвий перенос рядка в кінці
        return f"User: {self.user}\nItems:\n{items_list.rstrip()}"


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
# print(lemon)  # Виведе: lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
# print(buyer)  # Виведе: Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

# Виведе:
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього має бути 60"

cart.add_item(apple, 10)
print(cart)

# Виведе:
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.


assert cart.get_total() == 40, "Після зміни кількості яблук має бути 40"
