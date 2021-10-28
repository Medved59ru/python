import pickle
from string import punctuation

# На входе – текстовый файл с некоторым текстом на любом языке.
w = 0
t: str = ' '
with open('test.txt', 'rt+', encoding='utf-8') as file:
    t = file.read()

# считаем количество слов
sentences = t.split('.')
print(sentences)
quatityOfSentences = len(sentences)-1 # количество предложений
print(quatityOfSentences)

listOfWords =list(map(lambda x: len(x.split()), sentences)) # список количества слов использование mар в примере ниодного нет
totalQuantityOfWords = sum(listOfWords) # количество слов в предложений

text = t.replace('.', '')
text = text.replace(',', '')
words = text.split()
t= t.replace('-', '')

resultDict = {
    "Всего слов": totalQuantityOfWords,
    "Всего предложений": quatityOfSentences,
    "Предложения": [(sentence, len(sentence.split())) for sentence in sentences],
    "Слова": {word: len(word) for word in words},
    "Знаки препинания": {punct: t.count(punct) for punct in punctuation if t.count(punct)}
}

with open("resultDict.bin", mode="wb") as file:
    pickle.dump(resultDict, file)
with open("resultDict.bin", mode="rb") as file:
    resultDict = pickle.load(file)
# далее списано ... copy - past ибо изобретать велосипед не нужно ...
print(f"Всего слов: {resultDict['Всего слов']}")
print(f"Всего предложений: {resultDict['Всего предложений']}")
print("Предложения:")
for sentence, count in resultDict["Предложения"]:
    print(f"\t{sentence} {count}")
print("Слова:")
for word, count in resultDict["Слова"].items():
    print(f"\t{word} {count}")
print("Знаки препинания:")
for punct, count in resultDict["Знаки препинания"].items():
    print(f"\t{punct} {count}")

ok = False
while not ok:
    try:
        n = int(input("Введите n - количество предложений в абзаце: "))
        if n < 1:
            raise Exception
        ok = True
    except Exception as e:
        print("Необходимо ввести натуральное число!", end=" ")


paragraphs = [[]]
for sentence in sentences:
    if len(paragraphs[-1]) < n:
        paragraphs[-1].append(sentence)
    else:
        paragraphs.append([sentence])

paragraphs.sort(key=lambda paragraph: len([word for sentence in paragraph for word in sentence.split()]))

text = "\n".join([" ".join(paragraph) for paragraph in paragraphs]) # ох уж эта не строгая типизация - что попало можно делать

with open("resultText.txt", mode="w") as file:
    print(text, file=file)




