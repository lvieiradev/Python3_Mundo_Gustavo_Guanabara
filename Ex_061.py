numero = int(input("Digite um número: "))

fatorial = 1
i = numero

while i > 0:
    fatorial = fatorial * i
    i = i - 1

print(f"{numero}! = {fatorial}")