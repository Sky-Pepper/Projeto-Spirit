import random, time

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
tamanho = int(input("Digite a quantidade de caracteres: "))

senha = ""
for i in range(tamanho):
    caractere = random.choice(caracteres)
    senha += caractere

print("Gerando senha...")
time.sleep(5)
print("Sua senha foi gerada:", senha)
