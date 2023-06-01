while True:
    inicio = int(input("Descubra a média entre idades(digite 1 para continuar): "))
    if inicio == 1:
        break
somaMulheres = 0
somaHomens = 0
mulheres = 0
homens = 0
soma = 0
for i in range(1, 11):
    genero = str(input("Digite o seu gênero(M para masculino e F para feminino: "))
    idade = int(input("Digite a idade: "))
    soma += idade
    if genero.upper() == "M":
        somaHomens += idade
        homens += 1
    elif genero.upper() == "F":
        somaMulheres += idade
        mulheres += 1
mediaMulheres = somaMulheres / mulheres
mediaHomens = somaHomens / homens
media = soma / 10
print(f"A média de idades das mulheres é: {mediaMulheres}")
print(f"A média de idades dos homens é: {mediaHomens}")
print(f"A média de idades é: {media}")
