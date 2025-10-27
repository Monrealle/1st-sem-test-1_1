def luhn_check(number_card):
    """
    Проверяет ввод по алгоритму Луна

    Args:
        numbee_card: Номер карты в виде строки или числа
                     Может содержать пробелы и другие символы
    Return:
        True: Если номер карты корректен
        False: Если номер карты неправильный
    """
    # Убираем все нецифровые символы
    digits = [int(d) for d in str(number_card) if d.isdigit()]

    control = digits.pop() # Контрольная цифра
    parity = (len(digits)) % 2
    total = 0

    for i in range(len(digits)):
        if i % 2 == parity:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]

    return (total + control) % 10 == 0

def main():
    """Консольная утилита на основе алгоритма Луна для проверки номеров карт"""
    print("Введите номер карты или -1 для выхода:")

    while True:
        try:
            user_input = input("> ").strip()

            # Проверяем ввод на наличие -1
            if user_input == '-1':
                print("Выход из программы")
                break

            # Проверяем, что ввод не пустой
            if not user_input:
                print("Ошибка, введите номер карты")
                continue
            # Проверяем номер карты
            if luhn_check(user_input):
                print("Correct")

            else:
                print("Incorrect")

        except KeyboardInterrupt:
            print("\nВыход из программы")
            break

if __name__ == "__main__":
    main()
