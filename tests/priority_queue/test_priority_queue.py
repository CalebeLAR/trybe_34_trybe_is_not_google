import pytest
from ting_file_management.priority_queue import PriorityQueue

mock_hight_priority = {'qtd_linhas': 4}
mock_regular_priority1 = {'qtd_linhas': 6}
mock_regular_priority2 = {'qtd_linhas': 10}


def test_basic_priority_queueing():
    """Testa as instancias da classe PriotityQueue"""

    # O teste rejeita implementações que não validam a funcionalidade de cada
    # método;
    priorityQueue = PriorityQueue()
    assert len(priorityQueue) == 0

    priorityQueue.is_priority(mock_hight_priority) is True
    priorityQueue.is_priority(mock_regular_priority1) is False

    priorityQueue.enqueue(mock_regular_priority1)
    priorityQueue.enqueue(mock_hight_priority)
    priorityQueue.enqueue(mock_regular_priority2)
    assert len(priorityQueue) == 3

    # O teste rejeita implementações que tratam todos os elementos com a mesma
    # prioridade;
    assert priorityQueue.dequeue() == mock_hight_priority
    assert priorityQueue.search(0) == mock_regular_priority1
    assert priorityQueue.search(1) == mock_regular_priority2

    priorityQueue.enqueue(mock_hight_priority)
    assert priorityQueue.search(0) == mock_hight_priority
    assert priorityQueue.search(1) == mock_regular_priority1
    assert priorityQueue.search(2) == mock_regular_priority2

    # O teste rejeita implementações que não levantam exceção ao acessar
    # índices inválidos para Filas;
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priorityQueue.search(3)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priorityQueue.search(-1)
