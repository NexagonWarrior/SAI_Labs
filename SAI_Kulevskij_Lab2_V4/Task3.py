def get_fibonacci_set(limit):
    fib_set = {1, 2}
    a, b = 1, 2
    while b <= limit:
        a, b = b, a + b
        fib_set.add(b)
    return fib_set


try:
    raw_input = input("Введіть цілі числа через кому: ")
    input_numbers = [int(x.strip()) for x in raw_input.split(',')]

    if not input_numbers:
        print("Список порожній.")
    else:
        max_val = max(input_numbers)
        fib_numbers = get_fibonacci_set(max_val)
        result = [num for num in input_numbers if num in fib_numbers]

        if result:
            print(f"Числа Фібоначчі з вашого списку: {', '.join(map(str, result))}")
        else:
            print("Серед введених чисел немає чисел Фібоначчі.")

except ValueError:
    print("Помилка! Переконайтеся, що ви вводите лише цілі числа, розділені комами.")