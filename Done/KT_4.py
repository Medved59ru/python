from tkinter import WORD, Button, Tk, END, Text
import bs4
import requests
import re

URL = r"http://lib.ru/PROZA/"

'''response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('small', class_='b')
print(quotes)'''


def reParse():
    response = requests.get(URL)
    htmlCode = response.text
    soup = bs4.BeautifulSoup(htmlCode, features="lxml")
    text = soup.get_text()
    textForT =re.sub("[(|)|\[|\]|dir|www]", "", text)
    return textForT.strip()

def buttonClick(ctrl, method):
    """Универсальный обработчик нажатия кнопки"""
    ctrl.delete("1.0", END)
    ctrl.insert(END,  reParse())

form = Tk()
form.title("КТ 4, вариант 1")
editText = Text(height=30, width=70, wrap=WORD)
editText.pack()
# bsButton = Button(text="Спарсить библиотекой", command=lambda: buttonClick(editText, method="bs"))
# bsButton.pack()
reButton = Button(text="Спарсить регулярками", command=lambda: buttonClick(editText, method="re"))
reButton.pack()

form.mainloop()