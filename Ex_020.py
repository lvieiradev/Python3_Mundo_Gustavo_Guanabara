import random
aluno_1 = input("Digite o nome do primeiro aluno: ")
aluno_2 = input("Digite o nome do segundo aluno: ")
aluno_3 = input("Digite o nome do terceito aluno: ")
aluno_4 = input("Digite o nome do quarto aluno: ")
opcoes = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteado = random.choice(opcoes)

print(f"O aluno sorteado para te ajudar foi: {sorteado} ")