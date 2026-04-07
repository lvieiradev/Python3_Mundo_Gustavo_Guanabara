salario = float(input("Digite o seu sálario atual: "))
if salario > 1250.00:
    salario = salario * 1.1
else:
    salario = salario * 1.15

print(f"Seu novo sálario é: {salario}")