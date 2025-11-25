import random
n = input("Вітаю у грі вгадай число введіть свій нікнейм ")
print(f"Привіт, {n} Я загадав число від 1 до 50 вгадай його")
s = random.randint(1, 50)
i = 1
while True:
    g = input("Введіть ваше число ")
    if not g.isdigit():
        print("Помилка потрібно ввести саме число")
    g = int(g)
    if g < s:
        print("Більше")
        i += 1
    elif g > s:
        print("Менше")
        i += 1
    else:
        print(f"Вітаю, {n} ви вгадали число {s} {i}")
        break

