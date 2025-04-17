def efszdf(number):
    number = 10.0
    number1 = int(number)
    num = 0
    square = []
    for num in range(number1):
        num + 1
        num2 =(num*num)
        print(num2)
        if num2 > 50:
            print(f"Квадрат числа {num} больше 50")
        if num2 < 20:
            print(f"Квадрат числа {num}  меньше 20")
        if  num2 >= 20 and num2 <=50:
            print(f"Квадрат числа {num} больше или равен 20 и меньше или равен 50")
        if num == 4:
            continue
        elif num == 9:
            break
    
        square.append(num2)
    print(square)
    return square
        
    variable = "Не пусто"
    if variable == "":
        raise ValueError("Пустая строка")
    print(square)

    
efszdf(number = 10.0)
square1 = efszdf(number = 10.0)
print(square1)
