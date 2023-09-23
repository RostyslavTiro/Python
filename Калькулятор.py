# Ця функція додає два числа
def add(x, y):
    return x + y

# Ця функція віднімає два числа
def subtract(x, y):
    return x - y

# Ця функція множить два числа
def multiply(x, y):
    return x * y

# Ця функція ділить два числа
def divide(x, y):
    return x / y


print("Виберіть дію:")
print("1.Обчислення")
print("2.Віднімання")
print("3.Множення")
print("4.Ділення")

while True:
    #Приймаємо вибір
    choice = input("Виберіть дію:(1/2/3/4): ")

    #Перевіряємо чи вибрано один з чотирьох варіантів
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка. Введіть число.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Перевіряємо чи хоче користувач новий розрахунок , якщо ні , то розриваємо цикл while
        next_calculation = input("Робімо наступний розрахунок? (так/ні): ")
        if next_calculation == "ні":
          break
    else:
        print("Помилка")