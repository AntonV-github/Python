inputResult = list(input("Введите слова через пробел: \n ").lower().split())
words = {}
for count in inputResult:
    words[count] = words.setdefault(count, 0) + 1
maximumValue = max(words.values())
for key in words.keys():
    if (words[key] == maximumValue):
        print (key, "-", maximumValue)
