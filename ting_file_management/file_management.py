import os
import sys


def txt_importer(path_file):
    """deve receber um caminho para um arquivo txt e retornar um array com
    cada linha do texto, deve tratar erros ao abrir e ler o arquivo"""

    # Verifica se o arquivo existe
    if not os.path.exists(path_file):
        # o método os.path.exists verifica se o caminho para o arquivo existe
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []

    # Verifica se o arquivo é no formato .txt
    if not path_file.lower().endswith(".txt"):
        # o método sys.stderr.write é similar ao print, porém é utilizado
        # para informar saidas de erro ou alertas e imprime no terminal sem
        # quebras de linha
        sys.stderr.write("Formato inválido\n")
        return []

    with open(path_file, 'r') as file:
        unformatedLines = file.read().split("\n")
        return unformatedLines
