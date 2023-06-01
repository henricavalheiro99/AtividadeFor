while True:
    inicio = int(input("Descubra o mais velho(digite 1 para continuar): "))
    if inicio == 1:
        break
maiorIdade = 0
nomeMaisVelho = ""
numeroMulheres = 0
for i in range(1, 9):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    genero = str(input("Digite o seu gênero(M para masculino e F para feminino: "))
    if genero.upper() == "M":
        if idade > maiorIdade:
            maiorIdade = idade
            nomeMaisVelho = nome

    if genero.upper() == "F":
        if idade < 20:
            numeroMulheres += 1


print(f"O homem mais velho é {nomeMaisVelho} com {maiorIdade} anos")
print(f"O número de mulheres com menos de 20 anos é {numeroMulheres}")
