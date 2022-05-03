import Adivinhação
import Calculadora
import Forca

def escolhe_jogo ():
    print ("*********************************")
    print ("***********Bem-vindo!************")
    print ("*********************************")
    print ("********Escolha seu jogo!********")
    print ("*********************************")

    print ("(1) Forca (2) Advinhação (3) Calculadora")
    jogo = int(input("Qual Jogo? "))

    if (jogo == 1):
        print ("Você escolheu o jogo da Forca!")
        Forca.jogar ()
    elif (jogo == 2):
        print ("Você escolheu o jogo da Adivinhação!")
        Adivinhação.jogar ()
    elif (jogo == 3):
        print ("Você escolheu a calculadora!")
        Calculadora.jogar ()

if(__name__ == "__main__"):
    escolhe_jogo()