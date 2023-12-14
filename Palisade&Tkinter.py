from tkinter import *
from tkinter import messagebox


def clicked(word, key): #Функція шифрування зі словом та ключем
    word = str(word).replace(" ", "")
    chars = dict() 
    result = "" #Створюємо результат , але ми отримаємо його в нормальній формі в кінці

    if key > len(word): #Якщо ключ більший за довжину слова
        key = key - (len(word) * (key // len(word)))

    if not key: 
        return

    for i in range(key): #В діапазоні ключа ми робимо списки 
        chars[i] = list()

    for num in range(0, len(word), key): #Вибираємо індекси букв 
        for i in range(key): #В діапазоні ключа
            if len(word) > num + i: #Якщо довжина слова більше індексу та змінної 
                chars[i] += word[num + i] #Додаємо в певний список

    shiphred_list = list(chars.values())#Метод values()повертає об’єкт, який відображає список усіх значень у словнику.
    shiphred_list.reverse()#Перевернути список зашифрованих елементів

    for i in shiphred_list: #
        result += "".join(i) #Отримуємо результат у вигляді рядка

    messagebox.showinfo(title="Результат", message=f"Зашифрований текст: {result}")


window = Tk()

TextLabel = Label(window, text="Введіть текст:")
TextLabel.pack()

TextEntry = Entry(window)
TextEntry.pack()

KeyLabel = Label(window, text="Введіть ключ:")
KeyLabel.pack()

KeyEntry = Entry(window)
KeyEntry.pack()

EnterButton = Button(window, text="Виконати", command=lambda: clicked(TextEntry.get(), int(KeyEntry.get()))) # під lambda ми розуміємо нашу функцію
EnterButton.pack()



window.mainloop()
def cipher(word, key): #Функція шифрування
    s = dict() 
    result = "" #Створюємо результат , але ми отримаємо його в нормальній формі в кінці 

    for i in range(key): #В діапазоні ключа ми робимо списки 
        s[i] = list()

    for num in range (0, len(word), key): #Вибираємо індекси букв 
        for i in range(key):
            if len(word) > num + i: #Якщо довжина слова більше індексу та змінної 
                s[i] += word[num + i] #Додаємо в певний список

    shiphred_list = list(s.values()) #Метод values()повертає об’єкт, який відображає список усіх значень у словнику.
    shiphred_list.reverse() #Перевернути список зашифрованих елементів

    for i in shiphred_list :
        result += "".join(i) #Отримуємо результат у вигляді рядка
    return result


while True :
    word = input("Введіть послання: ") # ввід послання
    key = int (input("Введіть ключ: ")) # ввід ключа
    print(cipher(word, key)) # виводимо шифрування

