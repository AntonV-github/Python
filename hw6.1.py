def findnum(n):
    string = str(n)
    return string == string[::-1]
a = 0
for i in range(1, 1000000, 2):
    if findnum(i) & findnum(f"{i:b}"):
        a += i
print(a)