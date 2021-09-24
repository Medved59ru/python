#С клавиатуры вводится предложение из нескольких слов, разделенных пробелами.
#Отсортировать слова в предложении по длине.
#Пример:“Python is the best programming language”.“is the best Python language programming”

text = input("Введите текст: ")

print(f"Количество слов: {text.count(' ') + 1}")

l = text.split()
q=""

for i in sorted(l,key=lambda a: len(a)):
    q = q + " " + i



print(f"Было: {text}")

print(f"Стало:  {q}")

