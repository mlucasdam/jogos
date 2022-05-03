def jogar ():
    print ("Calculadora")
    print ("Escolha uma das operações abaixo:")
    print ("1 - soma" , "2 - subtração" , "3 - multiplicação" , "4 - divisão" , "5 - Sair")

    operação_str = input ("escolha sua operação: ")
    operação = int(operação_str)

    operação_1 = 1
    operação_2 = 2
    operação_3 = 3
    operação_4 = 4
    opera_Sair = 5

    if operação == operação_1:
        print ("você escolheu a soma!")
        numero_1 = input ("Digite um numero: ")
        numero = int (numero_1)

        numero_2 = input ("Digite outro numero: ")
        numero = int (numero_2)

        soma = int(numero_1) + int(numero_2)
        print ("O Resultado é igual a:" , soma)   
    elif operação == operação_2:
        print ("você escolheu a subtração!")
        numero_1 = input ("Digite um numero: ")
        numero = int (numero_1)

        numero_2 = input ("Digite outro numero: ")
        numero = int (numero_2)

        subtração = int(numero_1) - int(numero_2)
        print ("O Resultado é igual a:" , subtração)
    elif operação == operação_3:
        print ("você escolheu a multiplicação!")
        numero_1 = input ("Digite um numero: ")
        numero = int (numero_1)

        numero_2 = input ("Digite outro numero: ")
        numero = int (numero_2)

        multiplicação = int(numero_1) * int(numero_2)
        print ("O Resultado é igual a:" , multiplicação)
    elif operação == operação_4:
        print ("você escolheu a Divisão!")
        numero_1 = input ("Digite um numero: ")
        numero = int (numero_1)

        numero_2 = input ("Digite outro numero: ")
        numero = int (numero_2)

        divisão = int(numero_1) / int(numero_2)
        print ("O Resultado é igual a:" , divisão)
    elif operação == opera_Sair:
        print ("Obrigado por usar a calculadora!")


if (__name__ == "__main__"):
    jogar ()