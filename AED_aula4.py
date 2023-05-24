
def ex8():
    x = 1
    while x <= 10:
        print(x)
        x = x + 1

def ex9():
    x = 10
    while x >= 1:
        print(x)

        x = x - 1

def ex10():
    x = 1
    while x <= 200:
        print(x)
        x = x + 1


def ex11():
    x = int(input("Insira um numero : "))
    n = 0
    while n <= 10:
        prod = x * n
        print(f"{x}x{n} == {prod}")
        n = n + 1


def ex12():
    n = int(input("Insira um número : "))
    cont = 1

    while cont <= n:
        print(str(cont) * cont)
        cont = cont + 1 


def ex13():
    n = int(input("Insira um número : "))
    cont = 1
    soma = 0
    while cont <= n:
        soma += cont
        cont += 1
    print(soma)

def ex14():
    n = int(input("Insira um número : "))
    cont = 2
    if n < 0:
        print("Número negativo")
    control = 0
    if n != 2 and n != 1 and n != 0:
        while cont < n:
            if n % cont == 0:
                print("Não primo")
                control += 1
                break
            cont += 1
        if control == 0:
            print("Primo")
    else:
        if n == 2:
            print("Primo")
        else:
            print("Não primo")

def ex15():
    n = int(input("Insira um número : "))
    cont = 2
    s1 = 0
    s2 = 1
    if n == 1:
        print(s1)
    else:
        if n == 2:
            print(s1)
            print(s2)
        else:
            print(s1)
            print(s2)
            while cont < n:
                fib = s1 + s2
                print(fib)
                s1 = s2
                s2 = fib
                cont +=1



def ex16():
    n = int(input("Insira um número: "))
    cont = n - 1
    prod = n * cont
    while cont > 1:
        cont = cont - 1
        prod = prod *cont

    print(prod)

if __name__ == "__main__":
    
    """print("Exercicio 8:")
    ex8()
    print("__________________________________")
    print("Exercicio 9:")
    ex9()
    print("__________________________________")
    print("Exercicio 10:")
    ex10()
    print("__________________________________")
    print("Exercicio 11:")
    ex11()
    print("__________________________________")
    print("Exercicio 12:")
    ex12()
    print("__________________________________")
    print("Exercicio 13:")
    ex13()
    print("__________________________________")
    print("Exercicio 14:")
    ex14()
    print("__________________________________")
    print("Exercicio 15:")
    ex15()"""
    print("__________________________________")
    print("Exercicio 16:")
    ex16()
