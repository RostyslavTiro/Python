text = input("Введіть букви чи слова:") 
if text == "букви": #Тут рахуємо букви
    list = input("Введіть букви:")#
    len = len(list) #довжина дорівнюватиме довжині списку
    print(len) 
    dict = {} #Словник
    for t in list: #Для змінної задаємо наступне 
        if(t.isalpha()): #Робить правдивим , якщо всі символи є буквами
            t = t.lower() #Виключаємо знаки та цифри , тобто рахуємо лише букви
            if t in dict:
                dict[t] += 1
            else :
                dict[t] = 1
    for letter, time in dict.items(): #Форматування у стовпець
        print(f"Буква: '{letter}', разів: '{time}'")

elif text == "слова": #Тут виводимо слова
    string = input("Введіть речення: ") #Робимо рядок для введення
    split_string = string.split() #Розділяємо рядок на список
    sort_string = [word for word in split_string if len(word) >= 3] #Робимо сортування
    set_string = set(sort_string) #Забираємо повторення
    my_list = list(set_string) #Список
    my_list.sort() #Сортуємо список
    length = int(len(my_list)) #Отримуємо довжину списку
    for i in range(length): #Задаємо як будемо показувати слова через цикл
        print(i + 1,": ", my_list[i], sep="") #Тут виглядає це ось так : 1: привіт
else: #Якщо не вибрано букви чи слова
    print("Помилка")