from matplotlib import pyplot as plt

years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2022]
users = [10, 16, 24, 38, 47, 51, 60, 89]


# Anos no eixo Y / Usuários no eixo X 
plt.plot(years, users, color='blue', marker='o', linestyle='solid')

# Título
plt.title("Usuários de Internet a cada 100 habitantes")

# Descrição lateral
plt.ylabel("Número de Usuários (%)")
plt.show()
