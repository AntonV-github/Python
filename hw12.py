def fib(n):
    memory = {1:1, 2:1}
    if n in memory:
        return memory[n]
    x = 3
    while x < n + 1:
        memory[x] = memory[x-1] + memory[x-2]
        x += 1
    return memory[n]

print(fib(5432))