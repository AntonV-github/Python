# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.

def convert(temperature, unit):

    def to_fahrenheit(temp):
                return (temp * 9 / 5) + 32

    def to_celsius(temp):
                return (temp - 32) * 5 / 9

    if unit.upper() == 'C':
        return (to_fahrenheit(temperature), 'F')
    elif unit.upper() == 'F':
        return (to_celsius(temperature), 'C')
    else:
        print("Введите корректную единицу измерения температуры: F или С")

print(convert(32, 'F'))
print(convert(-50, 'C'))
print(convert(200, 'F'))
print(convert(1000, ' '))