N = print("Digite o valor:")
N = float(input())


Resto1 = N / 1
moeda_1 = (Resto1 // 01.00)
string1 = "{} moeda(s) de R$ 1.00"

Resto050 = Resto1 / 0.50
moeda_050 = (Resto050 // 0.50)
string050 = "{} moeda(s) de R$ 0.50"

'''
Resto025 = N / 0.25
moeda_025 = int (Resto025 // 0.25)
string025 = "{} moeda(s) de R$ 0.25"

Resto010 = N / 0.10
moeda_010 = int (Resto010 // 0.10)
string010 = "{} moeda(s) de R$ 0.10"

Resto005 = N / 0.05
moeda_005 = int (Resto005 // 0.05)
string005 = "{} moeda(s) de R$ 0.05"

Resto001 = N / 0.01
moeda_001 = int ( Resto001// 0.01)
string001 = "{} moeda(s) de R$ 0.01"
'''

print("MOEDAS:")

print(string1.format(moeda_1))
print(string050.format(moeda_050))

'''
print(string025.format(moeda_025))
print(string010.format(moeda_010))
print(string005.format(moeda_005))
print(string001.format(moeda_001))
'''