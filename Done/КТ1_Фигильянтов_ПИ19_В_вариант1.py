#  Написать функцию, вычисляющую значение выражения:
#   где n – четное число (если введено нечетное, выводить сообщение об этом и просить ввести заново).
print("===Вычисляем значения выражения===")
try:
    n = int(input("Введите четное число n: "))

    while n%2 != 0:
        print(" Введено не четное число ")
        n = int(input("Введите четное число n: "))
    print(f"n = {n}")

    x = float(input("Введите число x: "))

    from math import sin, cos

    f = n
    s = n
    up=0.0
    down=0.0

    while f>=1:
        up=up+(sin(x**(f-1))-cos(x**f))
        f-=2
        print(f"up = {up}")
        
    while s>=1:
        down=down+(x**(1/s))
        s-=1
        print(f"down = {down}")

    S=up/down

   
    print(f"S = {S}", end= " ")

    
except: 
    print("Некорректный ввод! ", end= " ")

