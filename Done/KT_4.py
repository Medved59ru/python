import re
import bs4
import requests
import tkinter as tk

URL = r"http://lib.ru/PROZA/"

def bsParse():
    response = requests.get(URL)
    htmlCode = response.text
    soup = bs4.BeautifulSoup(htmlCode, features="lxml")
    tags = soup.find_all("li")[6:]
    rows =""
    for li in tags:
        author = li.find_all("b")[1].text
        number = li.find_all("small")[0].text
        number = re.sub("[(|)|\[|\]|dir|www]", "", number)
        rows += f"{number}\t{author}\n"
    return rows.strip()

def reParse():
    response = requests.get(URL)
    htmlCode = response.text
    soup = bs4.BeautifulSoup(htmlCode, features="lxml")
    text = soup.get_text()
    textForT =re.sub("[(|)|\[|\]|dir|www]", "", text)
    return textForT.strip()

def buttonClick(ctrl, method):
    """Универсальный обработчик нажатия кнопки"""
    ctrl.delete("1.0", tk.END)
    ctrl.insert(tk.END, bsParse() if method == "bs" else reParse())


form = tk.Tk()
form.title("КТ 4, вариант 7")
editText = tk.Text(height=30, width=70, wrap=tk.WORD)
editText.pack()
bsButton = tk.Button(text="Спарсить библиотекой", command=lambda: buttonClick(editText, method="bs"))
bsButton.pack()
reButton = tk.Button(text="Спарсить регулярками", command=lambda: buttonClick(editText, method="re"))
reButton.pack()

form.mainloop()