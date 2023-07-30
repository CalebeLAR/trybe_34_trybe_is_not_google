import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    """Essa função imprime no stdout do terminal um dicionario com informaçoẽs
    do arquivo no caminho path_file e insere ele na fila(Queue) caso ele já
    não esteja lá """

    # verifica se o arquivo ja existe na queue
    for element in instance.queue:
        if element['nome_do_arquivo'] == path_file:
            return None
            break

    dados_do_arquivo = txt_importer(path_file)

    # monta um dicionario com o resultado
    dicionario_com_resultado = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(dados_do_arquivo),
        'linhas_do_arquivo': dados_do_arquivo
        }

    instance.enqueue(dicionario_com_resultado)
    sys.stdout.write(f'{dicionario_com_resultado}\n')


def remove(instance):
    """essa função remove os primeiro elemento da fila passada a ela por
    parametro"""

    if not instance.queue:
        sys.stdout.write('Não há elementos\n')
        return None

    ultimo_arquivo_processado = instance.dequeue()
    path_file = ultimo_arquivo_processado['nome_do_arquivo']

    sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


