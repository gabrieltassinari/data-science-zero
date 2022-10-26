# Compreensão de listas
pairs = [(x, y) for x in range(10) for y in range(10)]

increasing_pairs = [(x, y) for x in range(10) for y in range(x + 1, 10)]


# Geradores
def count():
    yield 1
    yield 2
    yield 3

for item in count():
    print(item)


# Compactação de listas
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
new_list = list(zip(list1, list2))
print(new_list)