A,B,C,D = input().split(" ")

A = int(A)
B = int(B)
C = int(C)
D = int(D)

SomaAB = A + B
SomaCD = C + D
if B > C and D > A:
    if SomaCD > SomaAB:
        if SomaCD >= 0 and SomaAB >= 0:
            if (A % 2==0):
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")