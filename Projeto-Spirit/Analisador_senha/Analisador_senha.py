print("\033[30m-\033[m" * 20)
print("\033[1;34mAnalisador de senhas\033[m")
print("\033[30m-\033[m" * 20)

senha = input("\nDigite sua senha: ")

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
    qualidades.append("\033[34m✓ Tamanho adequado\033[m")

if tem_maiuscula:
    qualidades.append("\033[34m✓ Possui letra maiúscula\033[m")

if tem_minuscula:
    qualidades.append("\033[34m✓ Possui letra minúscula\033[m")

if tem_numero:
    qualidades.append("\033[34m✓ Possui número\033[m")

if tem_simbolo:
    qualidades.append("\033[34m✓ Possui símbolo\033[m")

print("\nQualidades da senha: ")

for qualidade in qualidades:
    print(qualidade)

pontos = len(qualidades)

defeitos =[]

if len(senha) < 8:
    defeitos.append("\033[31mX Tamanho inadequado\033[m")

if tem_maiuscula == False:
    defeitos.append("\033[31mX Não possui letra maiúscula\033[m")

if tem_minuscula == False:
    defeitos.append("\033[31mX Não possui letra minúscula\033[m")

if tem_numero == False:
    defeitos.append("\033[31mX Não possui número\033[m")

if tem_simbolo == False:
    defeitos.append("\033[31mX Não possui símbolo\033[m")

print("\nDefeitos da senha: ")

for defeito in defeitos:
    print(defeito)

if not defeitos:
    print("Nenhum")

if pontos == 5:
    print("\n\033[32mSua senha é: forte\033[m")

elif pontos >= 3:
    print("\n\033[33mSua senha é: mediana\033[m")

else:
    print("\n\033[31mSua senha é: fraca\033[m")