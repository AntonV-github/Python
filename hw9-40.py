
# Champernowne's constant

# Problem 40

print(eval('*'.join([''.join(str(i) for i in range(1, 200000))[i-1] for i in [10 ** i for i in range(7)]])))