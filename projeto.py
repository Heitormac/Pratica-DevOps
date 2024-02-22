from random import randint
 
chutes = 0
numero_aleatorio = int(randint(1,20))
 
acerto = True
 
while acerto:
    chutes += 1
    numero_chutado = int(input("Chute um numero inteiro de 1 a 20:"))
    if numero_chutado == numero_aleatorio:
        print("acertou!")
        print(f"Numero de chutes: {chutes}")
        acerto = False
    elif numero_chutado < 1 or numero_chutado > 20:
        print("Digite um numero válido!")
    else:
        if numero_chutado > numero_aleatorio:
            print(f"O numero secreto é menor que {numero_chutado}")
        else:
            print(f"O numero secreto é maior que {numero_chutado}")