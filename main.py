#################################################################################
# Primeiro programa em Python com o curso da WR Kits. Exercício livre.
# Software de geração de números aleatórios.
# Versão 1.0
# Data 09 / 07 / 2024
# Autor: Luciano Ronchini
#################################################################################
# Inicialização das bibliotecas e variáveis #####################################
import random
import string

z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
z6 = 0
acc_acertos = 0
rep = 0
num = False
################################################# Fim das bibliotecas e variáveis
# Início do programa
print("Sorteio de Números.")
print(" ")

x1 = int(input("Escolha o primeiro número: "))
x2 = int(input("Escolha o segundo número: "))
x3 = int(input("Escolha o terceiro número: "))
x4 = int(input("Escolha o quarto número: "))
x5 = int(input("Escolha o quinto número: "))
x6 = int(input("Escolha o número bonus: "))

y1 = random.randint(1,20)
y2 = random.randint(1,20)
y3 = random.randint(1,20)
y4 = random.randint(1,20)
y5 = random.randint(1,20)
# Evitar que sejam sorteados números repetidos
while y2 == y1:
    y2 = random.randint(1, 10)
while ((y3 == y2) or (y3 == y1)):
    y3 = random.randint(1,10)
while ((y4 == y3) or (y4 == y2) or (y4 == y1)):
    y4 = random.randint(1, 10)
while ((y5 == y4) or (y5 == 3) or (y5 == y2) or (y5 == y1)):
    y5 = random.randint(1, 10)

sortear = int(input("Realizar sorteio? (1 = Sim / 0 = Não): "))
print(" ")
if sortear == 1:

    # Verificando primeiro número
    if (x1 == y1) or (x1 == y2) or (x1 == y3) or (x1 == y4) or (x1 == y5):
        #print("#1 numero a considerar")
        z1 = x1
        acc_acertos = acc_acertos + 1

    # Garantindo que os numeros de 1 a 5 não sejam iguais
    if x2 != x1:
        if (x2 == y1) or (x2 == y2) or (x2 == y3) or (x2 == y4) or (x2 == y5):
            #print("#2 numero a considerar")
            z2 = x2
            acc_acertos = acc_acertos + 1
    else:
        rep = rep + 1

    if (x3 != x1) and (x3 != x2):
        if (x3 == y1) or (x3 == y2) or (x3 == y3) or (x3 == y4) or (x3 == y5):
            #print("#3 numero a considerar")
            z3 = x3
            acc_acertos = acc_acertos + 1
    else:
        rep = rep + 1

    if (x4 != x1) and (x4 != x2) and (x4 != x3):
        if (x4 == y1) or (x4 == y2) or (x4 == y3) or (x4 == y4) or (x4 == y5):
            #print("#4 numero a considerar")
            z4 = x4
            acc_acertos = acc_acertos + 1
    else:
        rep = rep + 1

    if (x5 != x1) and (x5 != x2) and (x5 != x3) and (x5 != x4):
        if (x5 == y1) or (x5 == y2) or (x5 == y3) or (x5 == y4) or (x5 == y5):
            #print("#5 numero a considerar")
            z5 = x5
            acc_acertos = acc_acertos + 1
    else: # rep é um contador de números repetidos para que os números coincidentes não sejam considerados mais de uma vez
        rep = rep + 1

    # Inserindo a condição do número bonus para que seja considerado somente se for necessário
    if (x6 != x1) and (x6 != x2) and (x6 != x3) and (x6 != x4) and (x6 != x5):
        if x6 == y1:
            #print("#6 numero a considerar")
            acc_acertos = acc_acertos + 1
            z6 = x6
        elif x6 == y2:
            #print("#6 numero a considerar")
            acc_acertos = acc_acertos + 1
            z6 = x6
        elif x6 == y3:
            #print("#6 numero a considerar")
            acc_acertos = acc_acertos + 1
            z6 = x6
        elif x6 == y4:
            #print("#6 numero a considerar")
            acc_acertos = acc_acertos + 1
            z6 = x6
        elif x6 == y5:
            #print("#6 numero a considerar")
            acc_acertos = acc_acertos + 1
            z6 = x6
        else: # Necessáro zerar o x6 (bonus) para que ele seja exibido somente se bateu com o sorteio
            z6 = x6 # Para exibir a escolha do número bonus ao final, foi criada outra variável, z6
            x6 = 0
    else: # Se o número bonus for repetido então é ignorado
        rep = rep + 1
        z6 = x6
        x6 = 0
        print("O numero bonus foi repetido, por isso será ignorado.")
        print(" ")

    # Condição de vitória
    if z1 != 0 and z2 != 0 and z3 != 0 and z4 != 0 and z5 != 0:
        print("Parabéns, você ganhou!!!")
        print("Sorteio: " + str(y1) + " " + str(y2) + " " + str(y3) + " " + str(y4) + " " + str(y5))
        print(" ")
    else: # Condição de derrota
        print("Você não acertou todos números.")
        print(" ")
        print("Resultados: ")
        print("      Sorteio: "+ str(y1) + " " + str(y2) + " " + str(y3) + " " + str(y4) + " " + str(y5))
        print("      Suas escolhas: " + str(x1) + " " + str(x2) + " " + str(x3) + " " + str(x4) + " " + str(x5) + " " + str(z6))
        #                                                        # z6 é exibido sempre pois representa a escolha do número bonus

    # Acumulador de acertos conta quantos números escolhidos coincidiram com o sorteio
    if acc_acertos != 0:
        print("Você obteve " + str(acc_acertos) + " acertos: ")
        if z1 != 0:
            print("   Numero " + str(z1))
        if z2 != 0:
            print("   Numero " + str(z2))
        if z3 != 0:
            print("   Numero " + str(z3))
        if z4 != 0:
            print("   Numero " + str(z4))
        if z5 != 0:
            print("   Numero " + str(z5))
        if x6 != 0:
            print("   Numero " + str(x6)) # É exibido somente se bateu com o sorteio
    else:
        print(" ")
        print("Não houve acertos")

    # Exibe a quantidade de números repetidos caso tenha ocorrido
    if rep != 0:
        print("Você repetiu " + str(rep) + " números nas suas escolhas.")

else:
    print("Programa finalizado.")


#print(str(z1)+str(z2)+str(z3)+str(z4)+str(z5)+str(x6))

