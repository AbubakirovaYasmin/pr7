def convert_number():
    user_input = input("Введите десятичное число (или 'q' для выхода): ")

    if user_input.lower() == 'q':
        print("Выход из программы.")
    else:
        try:
           
            decimal_number = int(float(user_input)) 
            binary_number = bin(decimal_number)[2:] 
            octal_number = oct(decimal_number)[2:]  
            
           
            print(f"Двоичное представление: {binary_number}")
            print(f"Восьмеричное представление: {octal_number}")
        
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное десятичное число.")

convert_number()