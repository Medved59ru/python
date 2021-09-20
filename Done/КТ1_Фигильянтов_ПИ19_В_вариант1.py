#  Написать функцию, вычисляющую значение выражения:
#   где n – четное число (если введено нечетное, выводить сообщение об этом и просить ввести заново).
print("===Вычисляем значения выражения===")
try:
    n = int(input("Введите четное число n: "))

    while n%2 != 0:
        print(" Введено не четное число ")
        n = int(input("Введите четное число n: "))
    print(f"n = {n}")

    x = float(input("Введите число (градусы) x: "))

    
    from math import sin, cos, radians

    x=radians(x)

   # print(f"x = {x}")
    up=0.0
    down=0.0

    while n>1:
        up=up+(sin(x**(n-1))-cos(x**n))
        down=down+(x**(1/n))
        n-=1

    S=up/down
    
    print(f"S = {S}", end= " ")

    
except: 
    print("Некорректный ввод! ", end= " ")

