while True:
    inicio = int(input("Descubra os divisíveis de 7(digite 1 para continuar): "))
    if inicio == 1:
        break
num = 0
for i in range(5, 101):
    if i % 7 == 0 and i % 5 !=0:
        print(f"{i} é um número requerido")
        num += 1
print(f"O número de requeridos é {num}")