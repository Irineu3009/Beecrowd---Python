Lanche, Quantidade = input().split(" ")

Lanche_1 = int(Lanche)
Quantidade = int(Quantidade)

CQ = 1 # Cachorro-Quente -> Preço: R$ 4.00
X_S = 2 # X-Salada -> Preço: R$ 4.50
X_B = 3 # X-Bacon -> Preço: R$ 5.00
TS = 4  # Torrada Simples -> Preço: R$ 2.00
R = 5   # Refrigerante  -> Preço: R$ 1.50

if Lanche_1  == CQ:
    Valor1 = 4.00
elif Lanche_1 == X_S:
    Valor1 = 4.50
elif Lanche_1 == X_B:
    Valor1 = 5.00
elif Lanche_1 == TS:
    Valor1 = 2.00
elif Lanche_1 == R:
    Valor1 = 1.50

# -----------------------------------------------------#
Total = Valor1 * Quantidade
print(("Total: R$ ")+ format(Total, ".2f"))