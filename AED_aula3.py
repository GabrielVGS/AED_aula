def media():
    freq = float(input("Insira a frequência (%): "))
    if freq < 75:
        return "Rodou"
    else:
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        n4 = float(input("Nota 4: "))

        media = (n1+n2+n3+n4)/4

        if media >= 7:
            return "Aprovado"
        else:
            if media <= 3:
                return "Rodou"
            else:
                return "Exame"

def quad():
    l1 = float(input("Lado 1: "))
    l2 = float(input("Lado 2: "))

    if (l1 > 0) and (l2 > 0):
        print("São medidas válidas")
        if l1 == l2:
            return "É um quadrado"
        else:
            return "Não é quadrado"
    else:
        return "Medidas inválidas"



def camp():
    timeA = input("Time A")
    timeB = input("Time B")
    timeC = input("Time C")
    timeD = input("Time D")

    golsA_p1 = int(input("Gols do time A"))
    golsB_p1 = int(input("Gols do time B"))

    if golsA_p1 == golsB_p1:
        vencedor_p1 = input("Quem se classificou")
    else:
        if golsA_p1 > golsB_p1:
            vencedor_p1 = timeA
            print(f"Vendor da partida 1 {vencedor_p1}")
        else:
            vencedor_p1 = timeB
            print(f"Vencedor da partida 1 {vencedor_p1}")

    golsC_p1 = int(input("Gols do time C"))
    golsD_p1 = int(input("Gols do time D"))

    if golsC_p1 == golsD_p1:
        vencedor_p2 = input("Quem se classificou")
    else:
        if golsC_p1 > golsD_p1:
            vencedor_p2 = timeC
            print(f"Vencedor da partida 2 {vencedor_p2}")
        else:
            vencedor_p2 = timeD
            print(f"Vencedor da partida 2 {vencedor_p2}")
    
    print("Final do campeonato")
    gols_p3 = input(f"gols do {vencedor_p1} na final")
    gols_p4 = input(f"gols do {vencedor_p2} na final")

    if gols_p3 == gols_p4:
        vencedor_final = input("Quem venceu?")
    else:
        if gols_p3 > gols_p4:
            vencedor_final = vencedor_p1
        else:
            vencedor_final = vencedor_p2
    
    return f"Vencedor final : {vencedor_final}"


def IR(rend,corr):
    if corr == 'parcial':
        print("Correção no governo bolsonaro\n")
        if rend <= 2500.44:
            return 0
        else:
            if rend >= 2500.45 and rend <= 3712.16:
                par = rend - (7.5/100)* rend
                return par
            else:
                if rend >= 3712.17 and rend <= 4926.14:
                    par = rend - (15/100)* rend
                    return par
                else:
                    if rend >= 4926.15 and rend <= 6125.99:
                        par = rend - (22.5/100)* rend
                        return par
                    else:
                        par = rend - (27.5/100)* rend
                        return par
    else:
        if corr == 'integral':
            print("Correção integral\n")
            if rend <= 4710.49:
                return 0
            else:
                if rend >= 4710.5 and rend <= 6993.2:
                    par = rend - (7.5/100)* rend
                    return par
                else:
                    if rend >= 6993.21 and rend <= 9280.19:
                        par = rend - (15/100)* rend
                        return par
                    else:
                        if rend >= 9280.20 and rend <= 11540.53:
                            par = rend - (22.5/100)* rend
                            return par
                        else:
                            par = rend - (27.5/100)* rend
                            return par
        else:
            print("Sem correção\n")
            if rend <= 1903.98:
                return 0
            else:
                if rend >= 1903.99 and rend <= 2826.65:
                    par = rend - (7.5/100)* rend
                    return par
                else:
                    if rend >= 2826.66 and rend <= 3751.05:
                        par = rend - (15/100)* rend
                        return par
                    else:
                        if rend >= 3751.06 and rend <= 4664.68:
                            par = rend - (22.5/100)* rend
                            return par
                        else:
                            par = rend - (27.5/100)* rend
                            return par
            

lst = ["sem",'integral','parcial']

for tipo in lst:
    print(IR(2500,tipo))

