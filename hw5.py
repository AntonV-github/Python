numbers = list(map(int, input("Введите числа через пробел: \n").split()))
for i in range(min(numbers), max(numbers) + 2):
    if (not i in numbers):
        print(i)
        break
