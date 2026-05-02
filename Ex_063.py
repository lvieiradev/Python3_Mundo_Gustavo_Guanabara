while True:
    x = int(input("Digite o primeiro termo da PA: "))
    y = int(input("Digite a razão da PA: "))
    termos = int(input("Quantos termos você quer ver? "))

    i = 0
    while i < termos:
        print(x + (i * y))
        i = i + 1

    opcao = int(input("\nDigite 0 para sair ou qualquer número para continuar: "))
    if opcao == 0:
        print("Encerrando...")
        break