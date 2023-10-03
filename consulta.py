def read_n_digits(n):
    lst1 = []
    for _ in range(n):
        num = int(input("Digite um número:"))
        lst1.append(num)
    
    pos = []
    neg = []
    for i in lst1:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    return lst1,pos, neg


def remove_zeros(lst):
    lst1 = []
    for i in lst:
        if i != 0:
            lst1.append(i)
    return lst1

def make_matrix(m,n,val):
    matrix = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(val)
        matrix.append(line)
    return matrix

def divisors(n):
    divs = []
    for i in range(1,n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def expon(a,b):
    prod = 1
    for _ in range(b):
        prod *= a
    
    return prod

def sort_list(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] < A[j]:
                A[i],A[j] = A[j],A[i]
    return A


def merge_lists(A,B):
    C = A + B
    return sort_list(C)

def get_shape(A):
    return len(A),len(A[0])

def remove_duplicates(A):
    lst = []
    for i in A:
        if i not in lst:
            lst.append(i)
    return lst

def transpose(A):
    m,n = get_shape(A)
    B = make_matrix(n,m,0)
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]
    return B

def read_lines_and_turn_to_matrix(linha,coluna):
    matrix = []
    for _ in range(linha):
        linha = []
        for _ in range(coluna):
            val = int(input("Digite um número:"))
            linha.append(val)
        matrix.append(linha)
    return matrix

def get_max_value(A):
    max_val = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > max_val:
                max_val = A[i][j]
    return max_val

def matrix_array(shape: tuple, value: str) -> list:
    return [[value for _ in range(shape[1])] for _ in range(shape[0])]

def format_matrix(matrix: list) -> str:
    s = ""
    for line in matrix:
        s += " ".join(line) + "\n"
    return s

def jogo_da_velha():
    matrix = matrix_array((3,3),"-")
    for i in range(9):
        matrix_formated = format_matrix(matrix)
        print(matrix_formated)
        if i % 2 == 0:
            print("Vez do Jogador 1(X) : ")
            print("Digite a linha")
            linha = int(input())
            print("Digite a coluna")
            coluna = int(input())
            while linha > 2 or coluna > 2:
                print("Digite a linha")
                linha = int(input())
                print("Digite a coluna")
                coluna = int(input())
            matrix[linha][coluna] = "X"
        else:
            print("Vez do Jogador 2(O) : ")
            print(matrix_formated)
            print("Digite a linha")
            linha = int(input())
            print("Digite a coluna")
            coluna = int(input())
            while linha > 2 or coluna > 2:
                print("Digite a linha")
                linha = int(input())
                print("Digite a coluna")
                coluna = int(input())
            matrix[linha][coluna] = "O"


def max_value(A):
    max_val = A[0]
    for i in A:
        if i > max_val:
            max_val = i
    return max_val


def count_blanks(s):
    count = 0
    lst = []
    for i in s:
        if s == " ":
            count += 1
            lst.append(i)
        else:
            count = 0
    
    return max_value(lst)

def sum_matrix(A,B):
    C = []
    for i in range(len(A)):
        line = []
        for j in range(len(A[i])):
            line.append(A[i][j] + B[i][j])
        C.append(line)
    return C

def multiply_matrix(A,B):
    B = transpose(B)
    C = []
    for i in range(len(A)):
        line = []
        for j in range(len(B)):
            line.append(sum([A[i][k] * B[j][k] for k in range(len(A[i]))]))
        C.append(line)  


    return C


def quantosDias(dia,mes,ano):
    dia_atual,mes_atual,ano_atual = 1,1,1
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < ano_atual:
        return "Dia inválido"
    else:
        while dia_atual != dia or mes_atual != mes or ano_atual != ano:
            dia_atual += 1
            if dia_atual > 31:
                dia_atual = 1
                mes_atual += 1
            if mes_atual > 12:
                mes_atual = 1
                ano_atual += 1
        return dia_atual,mes_atual,ano_atual
