while True:
    inicio = int(input("Descubra o número de pares entre 1 e 100(digite 1 para continuar): "))
    if inicio == 1:
        break
num = 0
for i in range(1,101):
    if i %2 == 0:
        print(f"{i} é par")
        num += 1
print(f"O número de pares entre 1 e 100 é: {num}")