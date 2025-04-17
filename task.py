def efszdf(number):
    number = 10.0
    number1 = int(number)
    num = 0
    for num in range(number1):
        num + 1
        num2 =(num*num)
        print(num2)
        if num2 > 50:
            print(f"Квадрат числа {num} больше 50")
        if num == 4:
            continue
        elif num == 9:
            break
       
efszdf(number = 10.0)
efszdf(number = 18.0)
