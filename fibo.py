print("Фибоначчи итеративно")

list_fibo = [1, 1]

while True:
    number = input("Введите количество чисел Фибоначчи: ")
    try:
        number = int(number)
        if number < 1:
            print("Введите число больше 0")
            continue
        while len(list_fibo) < number:
            fibo_last = list_fibo[-1] + list_fibo[-2]
            list_fibo.append(fibo_last)
        print(f"Список чисел Фибоначчи: {list_fibo[:number]}")
        break
    except ValueError:
        print("Это не число, попробуйте снова")