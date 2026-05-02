soma = 0 
c = 1
n = int(input("Digite um número: "))
maior = n
menor = n
soma = n

while True:
    continua = str(input("Digite: 'S' para continuar ou 'N' para parar o programa: ")).upper()
    if continua == "N":
        break
    n = int(input("Digite um número: ")) 
    c += 1
    soma = soma + n
    if n < menor:
        menor = n
    if n > maior:
        maior = n 

media = soma / c 
print(f"A media dos numeros digitados foi de: {media}")
print(f"O maior numero digitado foi: {maior}")
print(f"O menor numero digitado é: {menor}")
