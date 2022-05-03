import random
def jogar ():
    print ("*********************************")
    print ("Bem-vindo ao jogo de adivinhação!")
    print ("*********************************")

    numero_secreto = random.randrange (101)
    total_de_tentativas = 0
    pontos = 1000

    print ("selecione sua dificuldade:")
    print ("(1) Facil (2) Médio (3) Dificil")

    nivel = int(input("Define o nivel: "))

    if (nivel == 1):
        total_de_tentativas = 20
        print ("Você tem 20 tentativas!")
    elif (nivel == 2):
        total_de_tentativas = 10
        print ("Você tem 10 tentativas!")
    else:
        total_de_tentativas = 5
        print ("Você tem 5 tentativas!")

    for rodada in range (1, total_de_tentativas + 1):
        print ("tentativas: {} / {}" .format(rodada, total_de_tentativas))
        chute_str = input ("Digite um numero entre 1 e 100: ")
        chute = int (chute_str)

        print ("você digitou" , chute)

        if (chute < 1 or chute > 100):
            print ("você deve digitar um numero entre 1 e 100")
            continue 

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print ("Você acertou! e fez {} pontos!!".format (pontos))
            break 
        else:
            if (maior):
                print ("Você errou! O seu chute foi maior que o seu numero secreto")
            elif (menor):
                print ("Você errou! O seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (rodada == total_de_tentativas):
                print ("O numero secreto era: {} e você fez: {} pontos".format(numero_secreto,pontos))
                


    print ("fim do jogo!")

if (__name__ == "__main__"):
    jogar ()