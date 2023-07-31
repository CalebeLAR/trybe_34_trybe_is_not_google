def linhas_onde_tem_a_palavra(index, word, line):
    lines = []
    for word_line in line.split(" "):
        if word.lower() == word_line.lower().replace(".", ""):
            lines.append({"linha": index + 1})
    return lines


def linhas_e_conteudo_onde_tem_a_palavra(index, word, line):
    lines = []
    for word_line in line.split(" "):
        if word.lower() == word_line.lower().replace(".", ""):
            lines.append({"linha": index + 1, "conteudo": line})
    return lines


def exists_word(word, instance):
    """Recebe uma palavra a ser pesquisada e uma fila com relatorios de
    arquivos. Retorna  uma lista com informações sobre os arquivos de onde a
    palavra foi encontrada"""
    arr = []

    for report in instance.queue:
        ocorrencias = []
        for index, line in enumerate(report['linhas_do_arquivo']):
            if linhas_onde_tem_a_palavra(index, word, line):
                new_line = linhas_onde_tem_a_palavra(index, word, line)
                ocorrencias.extend(new_line)

            result = {
                "palavra": word.lower(),
                "arquivo": report['nome_do_arquivo'],
                "ocorrencias": ocorrencias,
                }

        if result['ocorrencias']:
            arr.append(result)

    return arr


def search_by_word(word, instance):
    """Recebe uma palavra a ser pesquisada e uma fila com relatorios de
    arquivos. Retorna uma lista com informações sobre os arquivos de onde a
    palavra foi encontrada e o conteudo das linhas"""
    arr = []

    for report in instance.queue:
        ocorrencias = []
        for index, line in enumerate(report['linhas_do_arquivo']):
            if linhas_e_conteudo_onde_tem_a_palavra(index, word, line):
                new_line = linhas_e_conteudo_onde_tem_a_palavra(
                    index, word, line)
                ocorrencias.extend(new_line)

            result = {
                "palavra": word.lower(),
                "arquivo": report['nome_do_arquivo'],
                "ocorrencias": ocorrencias,
                }

        if result['ocorrencias']:
            arr.append(result)

    return arr
