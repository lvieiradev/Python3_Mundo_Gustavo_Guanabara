from math import hypot
cateto_o = float(input("Digite o comprimento do cateto oposto do triângulo retangalo: "))
cateto_a = float(input("Digite o comprimento do cateto adjacente : "))
hipotenusa = hypot(cateto_o, cateto_a)
print(f"O valor da hipotenusa é de: {hipotenusa}")
