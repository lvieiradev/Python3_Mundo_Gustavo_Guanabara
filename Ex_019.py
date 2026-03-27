import math
angulo = float(input("Digite o valor do angulo em graus: "))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
 
print(f"Para o Angulo de: {angulo}° os valores são os seguintes:")
print(f"O seno é: {seno:.4f}")
print(f"O cosseno é: {cosseno:.4f}")
print(f"A tangente é: {tangente:.4f}")