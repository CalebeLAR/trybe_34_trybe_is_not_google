import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Essa função imprime no stdout do terminal um dicionario com informaçoẽs
    do arquivo no caminho path_file e insere ele na fila(Queue) caso ele já
    não esteja lá """

    # verifica se o arquivo ja existe na queue
    for element in instance.queue:
        if element['nome_do_arquivo'] == path_file:
            return None
            break

    file_data = txt_importer(path_file)

    # monta um dicionario com o resultado
    result_dictionary = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_data),
        'linhas_do_arquivo': file_data
    }

    instance.enqueue(result_dictionary)
    sys.stdout.write(f'{result_dictionary}\n')


def remove(instance):
    """essa função remove os primeiro elemento da fila passada a ela por
    parametro"""

    if not instance.queue:
        sys.stdout.write('Não há elementos\n')
        return None

    last_processed_file = instance.dequeue()
    path_file = last_processed_file['nome_do_arquivo']

    sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """essa função apresentar as informações superficiais de um arquivo
    processado passando a posição dele por parametro"""

    if position >= instance.length:
        sys.stderr.write('Posição inválida\n')
        return None

    last_searched_file = instance.search(position)
    sys.stdout.write(f'{last_searched_file}\n')
