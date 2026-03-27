import random 
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceito nome: ")
nome4 = input("Digite o quarto nome: ")
nome5 = input("Digite o quinto nome: ")

alunos = [nome1, nome2, nome3, nome4, nome5]

random.shuffle(alunos)

print(f"O primeiro sorteado foi: {alunos[0]}")
print(f"O segunfo sorteado foi: {alunos[1]}")
print(f"O terceito sorteado foi: {alunos[2]}")
print(f"O quarto sorteado foi: {alunos[3]}")
print(f"O quinto sorteado foi: {alunos[4]}")