import random
def ex17():
    n = int(input("Digite um número"))
    control = 0
    cont = 0
    while n != 0:
        control += n
        cont +=1
        n = int(input("Digite um número"))

    media = control/cont
    print(media)

def ex19():
    sorteado = random.randint(0,10)
    print("Chute um número de 0 a 10")
    n = int(input())
    print(sorteado)
    while n != sorteado:
        n = int(input("tente de novo "))
    print("Acertou")

def ex20():
    n = int(input("Digite um número"))
    cont = 1

    while cont <= 6:
        if n%2 != 0:
            print(n)
            cont += 1
            n +=1
        else:
            n += 1
        

def ex21():
    x = int(input("digite um valor x :"))
    y = int(input("digite um valor y : "))
    n = 2
    cont = 0
    while not (x < y):
        x = int(input("digite um valor x :"))
        y = int(input("digite um valor y : "))

    while x < y:
        while n < x:
            if x%n == 0 and x!= 2:
                cont +=1
                n = n + 1
            else:
                n = n + 1

        if cont == 0 and x!= 1:
            print(x) 

        x = x + 1
        n = 2
        cont = 0

def ex22():
    n = 0
    acc = 0
    cont = 1
    maior = 0
    menor_c = 0
    while n < 7:

        #nome_atleta = input("Nome do atleta : ")
        nota_atleta =  float(input("Nota do atleta"))
        if nota_atleta < menor_c:
            menor_c = nota_atleta
        if nota_atleta > maior:
            maior = nota_atleta



        acc = nota_atleta + acc
        cont +=1
        n +=1

    nota_final = acc - (maior + menor_c)
    print(nota_final)
    print(acc)
    print(menor_c,maior)



def ex23():
    r = int(input("Selecione um intervalo"))
    n = 0
    while n < r:
        if len(str(n)) == 2 and "1" in str(n) and "2" in str(n) and n%3 == 0:
            print(n)
        n += 1


def ex24():
    n = 0
    u = 0
    d = 0
    c = 0
    while n <= 600: #10 min em segundos
        if u > 9:
            u = 0
            d +=1
        if d >= 6 :
            d = 0
            c +=1

        print(f"{c}:{d}{u}")
        u+=1
        n +=1

def ex25():
    tijolo = input("Informe o tijolo : ")
    andar = int(input("Andares : "))
    n = 1
    cont = 1
    c = andar
    while n < andar:
        print(" "*(c) + tijolo * cont + " "*(c))
        cont +=2
        n +=1
        c = c - 1

ex25() 
