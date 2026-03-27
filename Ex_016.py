q_dias = int(input("Digite quantos dias você ficou com o carro : "))
q_km = float(input("Digite quantos Km Você andou : "))
v_finaldias = q_dias * 60
v_kms = q_km * 0.15
print(f"O total de Kms andados foi de: {q_km},e o total de dias foi : {q_dias}")
print(f"Você gastou de diaria: {v_finaldias}, e de quilometragem : {v_kms}")