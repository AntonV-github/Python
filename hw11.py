def letters_range(start, stop, step=1):
    return [chr(x) for x in range(ord(start), ord(stop), step)]


print(letters_range('b', 'w', 2))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']

print(letters_range('a', 'g'))
# ['a', 'b', 'c', 'd', 'e', 'f']

print(letters_range('g', 'p'))
# ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

print(letters_range('p', 'g', -2))
# ['p', 'n', 'l', 'j', 'h']

print(letters_range('a', 'a'))
