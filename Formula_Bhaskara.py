import math

A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)
try:
    RQ1 = math.sqrt((B*B) - (4*A*C))
    X = (-B + RQ1)
    X1 = 2*A

    Y = (-B - RQ1)
    Y1 = 2*A

    R1 = X/X1
    R2 = Y/Y1

    print(("R1 = ") + format(R1, ".5f"))
    print(("R2 = ")+ format(R2, ".5f"))

except:
    print("Impossivel calcular")

