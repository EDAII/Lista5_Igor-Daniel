class Node:
    def __init__(self, data):
        self.data = data  # Representa o valor
        self.parent = None  # Representa o parente
        self.left = None  # Filho a esquerda
        self.right = None  # FIlho a direita
        self.color = 1  # Pode ser vermelha ou preta