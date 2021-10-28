"""
Инвест. проект заключается в том, чтобы научиться программировать
Регулярный доход:  500 долл. зарплата Junior C# разработчик
Регулярный расход: 150 долл. на зарплату за курсы + 390 долл. комуналка
Срок реализации проекта: 10 ЛЕТ
Ставка дисконтирования: 15 % уровень инфляции
"""
from itertools import accumulate
from functools import partial
import math


def calcNPV(cost0, income, cost, n, r):
    """Функция вычисляет NPV и DPP проекта"""

    NPVlist = [-cost0] + [(income - cost) / (1 + r) ** i for i in range(1, n + 1)]
    NPVaccum = list(accumulate(NPVlist))
    NPV = NPVaccum[-1]
    m = len([npvacc for npvacc in NPVaccum if npvacc < 0]) - 1
    DPP = m + abs(NPVaccum[m]) / NPVlist[m + 1] if len(NPVlist) > m + 1 else None
    return NPV, DPP


# входные данные
cost0 = 6000     # первоначальные затраты на учебу в ВШЭ
n = 10  # продолжительность проекта годы
income = 500*12*n  # Доходы от работы разработчиком в год
expensies = 490*12*n  # затраты на курсы программирования в месяц+комуналкa
r = 0.15

# считаем NPV, DPP
NPV, DPP = calcNPV(cost0, income, expensies, n, r)

# считаем IRR
calcNPV0 = partial(calcNPV, cost0=cost0, income=income, cost=expensies, n=n)
minNPV, IRR = math.inf, None
for r in range(1, 101):
    NPVirr = calcNPV0(r=r / 100)[0]
    if abs(NPVirr) < abs(minNPV):
        minNPV, IRR = NPVirr, r / 100
    print(r, NPVirr)

if IRR <= 0.01 or IRR >= 0.99:
    print("Скорее всего, IRR проекта с текущими параметрами отсутствует"
          " либо выбран слишком узкий диапазон изменения ставки дисконтирования")
    IRR = None

print("Учеба в ВЫШКЕ тот еще проект...")
print(f"ПРИВЕДЕННАЯ СТОИМОСТЬ = {NPV} USD, СРОК ОКУПАЕМОСТИ = {DPP} ЛЕТ, ДОПУСТИМЫЙ УРОВЕНЬ РЕАЛЬНОЙ ИНФЛЯЦИИ = {IRR*100} %: \n\tпроект {'' if NPV > 0 else 'не'}эффективен")
print("НО ЭТО НЕ ТОЧНО...")