N1, N2, N3, N4 = input().split(" ")
NotaExame = input()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

Media1 = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print(f"Media: {Media1:.1f}")

if Media1 >= 7.0:
    print("Aluno Aprovado.")
elif Media1 < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    print("Nota do exame:", NotaExame)
    Media1 = float(Media1)
    NotaExame = float(NotaExame)
    MediaFinal = Media1 + NotaExame
    MediaFinal = MediaFinal / 2
    if MediaFinal >= 5:
        print("Aluno aprovado.")
        print("Media final:", MediaFinal)
    else:
        print("Aluno Reprovado.")