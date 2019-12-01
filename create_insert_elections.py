import re
import pandas as pd

INSERT_ELEICAO = """
INSERT INTO ELEICAO (turno, idResultado, ano, cpf)
VALUES ('{}', {}, '{}', '{}');
"""

SELECT_RESULTADO = """
SELECT idResultado FROM RESULTADO WHERE descricaoResultado = '{}'
"""

#SELECT_CANDIDATURA_CPF = """
#SELECT cpf FROM CANDIDATURA WHERE cpf = '{}' AND ano = '{}'
#"""
#
#SELECT_CANDIDATURA_ANO = """
#SELECT ano FROM CANDIDATURA WHERE cpf = '{}' AND ano = '{}'
#"""


def create_insert_string(row):
    cpf = row[1]
    ano = row[2]
    idResultado = f"( {SELECT_RESULTADO.format(row[3])} )"
    turno = row[4]

    insert_sql = INSERT_ELEICAO.format(turno, idResultado, ano, cpf)

    return insert_sql


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_eleicoes.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()


def read_cpfs():
    regex = re.compile(r"(?P<cpf>\d+)(\t)(?P<year>\d{4})")
    f = open('candidaturas.txt', 'r')
    f = f.read().split('\n')
    cpf_year_list = []
    for x in f:
        match = regex.search(x)
        if match:
            cpf_year_list.append((match.group('cpf'), match.group('year')))

    return cpf_year_list


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return True
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x
    return False


if __name__ == '__main__':
    filename = 'new_candidates.csv'
    cpfs = read_cpfs()
    cpfs.sort()

    data = pd.read_csv(filename, usecols=['cpf', 'ano', 'descricaoResultado', 'turno'])
    counter = 0
    lines = []
    for row in data.itertuples():
        if binary_search(cpfs, (str(row[1]), str(row[2]))):
            line = create_insert_string(row)
            lines.append(line)

            counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
