print("Фибоначчи итеративно")

list_fibo = [1,1]

while True:
    number = input("Введите количество числа фибоначии")
    try:
        number = int(number)
        if number < 1:
            print("нельзя число ниже 1")
            continue
        while len(list_fibo) < number:
           fibo_last = list_fibo[-1] + list_fibo[-2]
           list_fibo.append(fibo_last)
        print(list_fibo)
        break
    except ValueError:
        print("не число")

