def get_integer(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value.is_integer():
                return int(value)
            else:
                choice = input("Вы ввели нецелое число. Использовать целую часть (да/нет)? ").strip().lower()
                if choice == 'да':
                    return int(value)
                elif choice == 'нет':
                    print("Ввод отменен.")
                    return None
                else:
                    print("Ошибка")
                    exit()
        except ValueError:
            print("Ошибка: введите число.")

def solve_equation(a, b, c):
    if b == 0:
        return "Ошибка: деление на ноль."
    x = (a / b) + (c * a)
    return x

a = get_integer("Введите значение a: ")
if a is None:
    exit()

b = get_integer("Введите значение b: ")
if b is None:
    exit()

c = get_integer("Введите значение c: ")
if c is None:
    exit()

result = solve_equation(a, b, c)
print(f"Результат уравнения: x = {result}")