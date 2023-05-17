def tri():
    try:
        l1 = float(input("Lado 1 :"))
        l2 = float(input("Lado 2 :"))
        l3 = float(input("Lado 3 :"))

        if (l1 > (l2 + l3)) or l2 > (l1 + l3) or l3 > (l2 + l1):
            return "Não pode formar triãngulo"
        else:
            if (l1 == l2) and (l1 == l3):
                return "Triangulo equilátero"
            else:
                if (l1 == l2) or (l1 == l3) or (l2 == l3):
                    return "Triangulo isosceles"
                else:
                    return "Triangulo escaleno"
    except ValueError:
        print("Válores númericos inválidos, insira-os novamente")
        return tri()


def max_tri():
        l1 = float(input("Lado 1 : "))
        l2 = float(input("Lado 2 : "))
        l3 = float(input("Lado 3 : "))

        maior = l1
        if l1 < l2 and l1 < l3:
            menor = l1
            if l2 < l3:
                meio = l2
                maior = l3
            else:
                meio = l3
                maior = l2
        else:
            if l2 < l3:
                menor = l2
                meio = l3
            else:
                menor = l3
                meio = l2

        return f"{menor}, {meio}, {maior}"


