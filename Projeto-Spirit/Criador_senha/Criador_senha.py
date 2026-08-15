print("-=-" * 5)
print("\033[1;32mGerador de senha\033[m")
print("-=-" * 5)


import random, time

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
tamanho = int(input("Digite a quantidade de caracteres: "))

senha = ""
for i in range(tamanho):
    caractere = random.choice(caracteres)
    senha += caractere

print("\033[36mGerando senha...\033[m")
time.sleep(5)
print("\033[36mSua senha foi gerada:\033[m", senha)
