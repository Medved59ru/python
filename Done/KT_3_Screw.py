'''Предетая область: Базовый класс - метизное изделие у него два наследника гайка и болт.
 Гайка расширяется материалов из которого сделана. Болт расширяется типом резьбы.'''

from dataclasses import dataclass
from random import randint

# конструктор базового класса Метиз
class Metalware:
    def __init__(self, name: str, quantity: int):
        self.__name = name  # имя
        self.__quantity = quantity  # количество
# поля
    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

# сеттер для количества
    @quantity.setter
    def quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise CustomError('Вы ввели отрицательное количество!')
            else:
                self.__quantity = quantity
        except ValueError:
            print('Ошибка при вводе количества, ввели не число')
        except CustomError as msg:
            print(msg)
# показать инофрмацию
    def display_info(self):
        print('Метиз:', self.__name, 'Количество: ', self.__quantity, 'шт')

    def __str__(self):
        return "Наименование: {} \t Количество: {} шт".format(self.__name, self.__quantity)

# сравнить
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__quantity == other.quantity

        else:
            print('Невозможно сравнить')
            return False
# добавить
    def __add__(self, other):
        return self.__quantity + other
# уменьшить
    def __sub__(self, other):
        return self.__quantity - other

# наследник Гайка
class Nut(Metalware):
    # конструктор
    def __init__(self, name, quantity, material: str):
        Metalware.__init__(self, name, quantity) # наследование
        self.material = material # расширение полей - добавляем тип материала

    # переопределение метода
    def display_info(self):
        print('Гайка', 'В количестве:', self.quantity, 'шт.', 'Материал:', self.material)


class Bolt(Metalware):
    # конструктор
    def __init__(self, name, quantity, shape: str):
        Metalware.__init__(self, name, quantity) # наследование
        self.shape = shape # расширение полей - добавляем тип резьбы
    # переопределяем метод
    def display_info(self):
        print('Болт', 'В количестве:', self.quantity, 'шт.', 'Резба:', self.shape)


# дата класс
@dataclass
class Set:
    nut_qty: int
    bolt_qty: int

# пользовательское исключение
class CustomError(Exception):
    def __init__(self, text):
        self.txt = text


# создаем экземпляры классов
metalware_example = Metalware('Mетизные изделия', 2)
nut = Nut('Гайка', 2, 'сталь 20')
one_more_nut = Nut('Гайка', 2, 'сталь 3')
bolt = Bolt('Болт', 2, 'М8')
# сравниваем экземпляры классов
print(metalware_example == nut)
print(metalware_example== metalware_example)
# переопределяем метод __str__
print(nut)
# используем свойства у экземпляров классов
nut.display_info()
metalware_example.display_info()
# дата класс
set_n_1 = Set(nut.quantity, bolt.quantity)
print(set_n_1)

#  проверяем работу исключения
metalware_new = Metalware("Тестовый болт", -2);
metalware_new.quantity = -5
metalware_new.quantity = 'asd'
print(metalware_new)


# Генератор гаек
def random_round_nut(quantity):
    while quantity > 0:
        quantity -= 1
        yield Nut("Гайка", randint(1, 10), f"сталь {quantity}")


generator = random_round_nut(5)
for i in generator:
    print(i.display_info())