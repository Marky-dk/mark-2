import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) #gera um número de 1 a 100

    numero_dificuldade = input("Digite o número da dificuldade: (1) para fácil, (2) para médio  e (3) para difícil : ")
    validar_dificuldade = int(numero_dificuldade)

    if(validar_dificuldade == 1):
        print("Você selecionou a opção (1)")
        total_de_tentativas = 20
    else:
        if(validar_dificuldade == 2):
            print("Você selecionou a opção (2)")
            total_de_tentativas = 10
        elif(validar_dificuldade == 3):
            print("Você selecionou a opção (3)")
            total_de_tentativas = 5
        elif(validar_dificuldade!=1 or validar_dificuldade !=2 or validar_dificuldade !=3):
            print("Por não saber responder uma pergunta que até o Patrick Estrela saberia, você tera 1000 chances")
            total_de_tentativas = 1000

    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute<1 or chute>100):
            print("Digite um número entre 1 a 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

    print("O número é: ", numero_secreto)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
