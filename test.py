from core.calc_core_wrapper import add, subtract, multiply, divide  # Импорт всех необходимых функций

def main():
    print("Добро пожаловать в CalcYouLater!")
    print("Введи 'exit' для выхода.")
    
    while True:
        user_input = input("Введи выражение (например, 2 + 3): ")

        if user_input.lower() == 'exit':
            print("До свидания!")
            break

        try:
            if '+' in user_input:
                numbers = user_input.split('+')
                if len(numbers) == 2:
                    a = float(numbers[0].strip())
                    b = float(numbers[1].strip())
                    result = add(a, b)
                    print(f"Результат: {result}")
                else:
                    print("АХТУНГ: введи два числа через '+'")
            elif '-' in user_input:
                numbers = user_input.split('-')
                if len(numbers) == 2:
                    a = float(numbers[0].strip())
                    b = float(numbers[1].strip())
                    result = subtract(a, b)
                    print(f"Результат: {result}")
                else:
                    print("АХТУНГ: введи два числа через '-'")
            elif '*' in user_input:
                numbers = user_input.split('*')
                if len(numbers) == 2:
                    a = float(numbers[0].strip())
                    b = float(numbers[1].strip())
                    result = multiply(a, b)
                    print(f"Результат: {result}")
                else:
                    print("АХТУНГ: введи два числа через '*'")
            elif '/' in user_input:
                numbers = user_input.split('/')
                if len(numbers) == 2:
                    a = float(numbers[0].strip())
                    b = float(numbers[1].strip())
                    result = divide(a, b)
                    print(f"Результат: {result}")
                else:
                    print("АХТУНГ: введи два числа через '/'")
            else:
                print("АХТУНГ: поддерживаются только операции: +, -, *, /")
        except ValueError:
            print("АХТУНГ: некорректный ввод. Пожалуйста, введи числа")

if __name__ == "__main__":
    main()
