import random

def jogo_de_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    while True:
        tentativa = int(input("Tente adivinhar o número (entre 1 e 10): "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")


jogo_de_adivinhacao()
