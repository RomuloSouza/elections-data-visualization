import pandas as pd
import bisect

MAX_CANDIDATES = 1000

INSERT_CANDIDATE = """
INSERT INTO CANDIDATO (cpf, nomeUrna, sexo, nomeCandidato, dtNascimento)
VALUES ('{}', '{}', '{}', '{}', {});
"""


def create_insert_string(row):
    dt = str(row[6])
    dt = f"'{dt[-4:]}-{dt[2:4]}-{dt[0:2]}'"
    if len(dt) != 12:
        dt = "NULL"

    nome_urna = str(row[3]).replace("'", "")
    nome_candidato = str(row[5]).replace("'", "")

    insert_sql = INSERT_CANDIDATE.format(
        row[2],
        nome_urna,
        row[4],
        nome_candidato,
        dt
    )

    return insert_sql


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


def create_cpfs_file(cpfs):
    f = open('cpfs.txt', 'w+')

    for cpf in cpfs:
        f.write(str(cpf)+'\n')

    f.close()


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_candidatos.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()


if __name__ == '__main__':
    filename = 'new_candidates.csv'

    data = pd.read_csv(filename, parse_dates=['dtNascimento'])
    counter = 0
    lines = []
    cpfs = []
    for row in data.itertuples():
        # if counter < MAX_CANDIDATES:
        cpf = row[2]
        if not binary_search(cpfs, cpf):
            bisect.insort(cpfs, cpf)

        counter += 1
        line = create_insert_string(row)
        lines.append(line)
        # else:
        #     break

    print('tamanho = ', counter)
    create_cpfs_file(set(cpfs))
    add_lines_to_file(lines)
