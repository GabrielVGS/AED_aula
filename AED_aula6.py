#numeros de digitos = 10
# (soma de digitos[0:9] % 10 ) = [-2]
# (soma de digitos[0:10] % 11 ) = [-1]

import random
def check_cpf(cpf):
    if len(cpf) != 11:
        return False
    
    reversed_cpf = cpf[::-1]
    reversed_halv_cpf = reversed_cpf[2:]

    mult = 2
    total = 0
    total2 = 0
    for j in reversed_halv_cpf:
        total = total + (mult*int(j))
        mult += 1
    
    resto = total % 11

    if resto < 2:
        primeiro = 0
    else:
        primeiro = 11 - resto

    reversed_halv_cpf = str(primeiro) + reversed_halv_cpf
    mult = 2
    for i in reversed_halv_cpf:
        total2 = total2 + (mult* int(i))
        mult +=1
    
    resto2 = total2 % 11

    if resto2 < 2:
        segundo = 0
    else:
        segundo = 11 - resto2
    
    if primeiro == int(cpf[9]) and segundo == int(cpf[10]):
        return True
    else:
        return False
    
def format_cpf(cpf):
    if check_cpf(cpf):
        cont = 0
        v = 0
        s = ""
        for char in cpf[0:9]:
            if cont == 3 and v < 2:
                s = s + "."
                cpf = cpf[cont:]
                cont = 0
                v = v + 1

            s = s + char
            cont = cont + 1

        cpf = cpf[3:]
        s = s + "-" + cpf
        return s
    else:
        return "CPF não é válido"


print(random.randint(0,9))

def generate_cpf():
    cpf = ""
    cont = 0

    while cont < 11:
        cpf = cpf + str(random.randint(0,9))    
        cont +=1
    
    return cpf

def generate_valid_cpf():
    cpf = generate_cpf()

    while not check_cpf(cpf):
        cpf = generate_cpf()
    
    return cpf



