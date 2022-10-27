from matplotlib import pyplot as plt

books = ["Ficção", "Romance", "Drama", "Filosofia", "Gastronomia"]
readed = [5, 10, 3, 11, 7]

xs = [i + 0.1 for i, _ in enumerate(books)]

# Barras com Largura [xs] / Altura [readed]
plt.bar(xs, readed)

# Altera a posição X das barras
plt.xticks([i + 0.1 for i, _ in enumerate(books)], books)

# Título
plt.title("Meus livros favoritos")

# Descrição lateral
plt.ylabel("# de Livros lidos")
plt.show()