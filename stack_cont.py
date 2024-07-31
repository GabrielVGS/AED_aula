class Pilha:
    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.lim = tamanho - 1  # Limite superior do vetor
        self.base = 0
        self.topo = self.base - 1  # Índice do topo, inicializado como -1 para indicar que a pilha está vazia

    def push(self, dado):
        if self.topo < self.lim:
            self.topo += 1
            self.vetor[self.topo] = dado
        else:
            raise IndexError("Pilha cheia")


    def pop(self):
        if self.topo != self.base -1:
            removed = self.vetor[self.topo]
            self.topo = self.topo -1
            return removed

        raise IndexError


    def vazia(self):
        if self.topo == self.base - 1:
            return True

        return False
    def get(self):
        if self.topo != self.base -1:
            return self.vetor[self.topo]


    def __str__(self):
        if self.vazia():
            return "Pilha vazia"
        return " -> ".join(str(self.vetor[i]) for i in range(self.base, self.topo + 1))



pilha = Pilha(5)
pilha.push("A")
pilha.push("B")
pilha.push("C")


print(pilha)  # Saída: A -> B -> C

print("Elemento removido:", pilha.pop())  # Saída: C
print(pilha)  # Saída: A -> B

pilha.push("D")
print(pilha)  # Saída: A -> B -> D
