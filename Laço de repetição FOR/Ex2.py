while True:
    inicio = int(input("Descubra a média entre temperaturas(digite 1 para continuar): "))
    if inicio == 1:
        break
clientes = int(input("Digite o número de clientes: "))
soma = 0
for i in range(1,clientes+1):
    temperatura = float(input("Digite o valor da temperatura: "))
    soma += temperatura
    if temperatura < 37.2:
        print(f"{temperatura}, está normal")
    elif temperatura >= 37.2 and temperatura <= 38:
        print(f"{temperatura}, está febril")
    elif temperatura > 38 and temperatura <= 39:
        print(f"{temperatura}, está com febre")
    else:
        print(f"{temperatura}, febre alta")
media = soma / clientes
print(f"A média das temperaturas é: {media}")
