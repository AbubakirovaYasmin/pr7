def decimal_to_nine_base(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number < 9:
        return str(decimal_number)
    else:
        return decimal_to_nine_base(decimal_number // 9) + str(decimal_number % 9)

def main():
    user_input = input("Введите целое число (или 'q' для выхода): ")

    if user_input.lower() == 'q':
        print("Выход из программы.")
        return

    try:
        decimal_number = int(float(user_input)) 
        nine_base_number = decimal_to_nine_base(decimal_number)
        print(f"Число {decimal_number} в девятеричной системе: {nine_base_number}")
    except ValueError:
        print("Ошибка: введите корректное целое число.")
        main() 

main()