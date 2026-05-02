c = 0 
soma = 0
while True: 
    n = int(input("Digite algum número: "))
    if n == 999:
        break
    soma = soma + n
    c += 1

print(f"\n A soma dos números digitados é {soma}")
print(f"\n Você digitou, {c} números")
