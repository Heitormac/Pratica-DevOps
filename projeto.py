#Feitor por Henry

#importando o randint da biblioteca random
from random import randint

#variavel contador que vai mostrar a quantidade de tentativas
chutes = 0

#usando o randint da biblioteca random
numero_aleatorio = int(randint(1,20))
 
acerto = True
#while que vai aumentar a quantidade de tentativas e repetir o codigo até o usuario acertar o numero misterioso
while acerto:
    chutes += 1
    numero_chutado = int(input("Chute um numero inteiro de 1 a 20: "))
    if numero_chutado == numero_aleatorio:
        print("acertou, parabens!!!")
        print(f"Numero de tentativas: {chutes}")
        acerto = False
    elif numero_chutado < 1 or numero_chutado > 20:
        print("Digite um numero válido, de 1 a 20!")
    else:
        if numero_chutado > numero_aleatorio:
            print(f"O numero secreto é menor que: {numero_chutado}")
        else:
            print(f"O numero secreto é maior que: {numero_chutado}")
#fim do programa
            