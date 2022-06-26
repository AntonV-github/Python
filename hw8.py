def userInput():
    number = input("Введите число: \n");
    if (number.lower() == 'cancel'): return "Bye!"
    try: value = int(number)
    except:
        print("Не удалось преобразовать введенный текст в число.")
        return userInput()
    return int(value / 2) if (value % 2 == 0) else value * 3 + 1
print(userInput())