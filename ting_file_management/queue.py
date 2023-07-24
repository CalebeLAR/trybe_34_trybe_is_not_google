from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()
        self.length = 0

    def __len__(self):
        """deve retornoar o tamanho atual da lista
        sem percorrer ela toda!"""
        return self.length

    def enqueue(self, value):
        """deve inserir um novo elemento no final da fila"""
        self.queue.append(value)
        self.length += 1

    def dequeue(self):
        """deve remover o elemento que está no inicio da fila"""

        if self.length == 0:
            # caso a fila esteja vazia retorna None
            return None

        self.length -= 1

        # pop(0) e del tem a mesma complexidade
        # pop(0) pode ser ligeiramente mais rápida que del
        return self.queue.pop(0)

    def search(self, index):
        """deve retornar o elemento que está na posição index passada
        por parâmentro"""

        if not isinstance(index, int):
            raise IndexError("Índice Inválido ou Inexistente")

        if index < 0 or index >= self.length:
            raise IndexError("Índice Inválido ou Inexistente")

        return self.queue[index]
