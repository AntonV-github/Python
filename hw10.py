def gipoteza(n):
    def loop(i, steps):
        if i == 1:
            return steps
        if i % 2 == 0:
            return loop(i // 2, steps+1)
        return loop(i * 3 + 1, steps+1)
    return loop(n, 0)

def collatz(n):
    result = gipoteza(n)
    print(f"Для вычисления последовательности Коллатца для числа {n} потребовалось {result} шагов.")

collatz(1)
collatz(3)
collatz(25)
collatz(1240)
collatz(1000)