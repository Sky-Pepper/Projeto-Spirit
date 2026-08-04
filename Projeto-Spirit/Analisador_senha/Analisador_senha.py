senha = input("Digite sua senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_simbolo = False

simbolos = "!@#$%&*?"

for caractere in senha:

    if caractere.isupper():
        tem_maiuscula = True

    if caractere.islower():
        tem_minuscula = True

    if caractere.isdigit():
        tem_numero = True

    if caractere in simbolos:
        tem_simbolo = True

qualidades = []

if len(senha) >= 8:
    qualidades.append("✓ Tamanho adequado")

if tem_maiuscula:
    qualidades.append("✓ Possui letra maiúscula")

if tem_minuscula:
    qualidades.append("✓ Possui letra minúscula")

if tem_numero:
    qualidades.append("✓ Possui número")

if tem_simbolo:
    qualidades.append("✓ Possui símbolo")

print("\nQualidades da senha: ")

for qualidade in qualidades:
    print(qualidade)

pontos = len(qualidades)

defeitos =[]

if len(senha) < 8:
    defeitos.append("X Tamanho inadequado")

if tem_maiuscula == False:
    defeitos.append("X Não possui letra maiúscula")

if tem_minuscula == False:
    defeitos.append("X Não possui letra minúscula")

if tem_numero == False:
    defeitos.append("X Não possui número")

if tem_simbolo == False:
    defeitos.append("X Não possui símbolo")

print("\nDefeitos da senha: ")

for defeito in defeitos:
    print(defeito)

if pontos == 5:
    print("\nSua senha é: forte")

elif pontos >= 3:
    print("\nSua senha é: mediana")

else:
    print("\nSua senha é: fraca")