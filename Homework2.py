        # 1. Квадрат числа
number = int(input("Input your number: "))
print (number ** 2)

        # 2. Середнє трьох чисел
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
result = ((n1 + n2 + n3)/3)
print(result)

        # 3. Перетворення хвилин у години
minutes = int(input("Enter time in minutes: "))
div, mod = divmod(minutes, 60)
print("It is", div, "hours and", mod, "minutes")

        # 4. Розрахунок знижки
price = float(input("Input price: "))
discount = int(input("Input discount amount (%): " ))
discounted_price = (price * (1 - discount / 100))
print(f"Discounted price: {discounted_price}")

        # 5. Остання цифра числа

number = int(input("Input three-digit number: "))
n3 = number % 10
print("Last number is: ", n3)

        # 6.  Периметр прямокутника

side_a = float(input("Input side 'a' of rectangle: "))
side_b = float(input("Input side 'b' of rectangle: "))
perimeter = ((side_a + side_b) * 2)
print("Perimeter of a rectangle equals ", perimeter)

        # 7. Виведення числа в стовпчик

number = int(input("Input four-digit number: "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 1000  % 100 // 10
n4= number % 1000 % 100 % 10
print(n1)
print(n2)
print(n3)
print(n4)