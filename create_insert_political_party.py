import pandas as pd

INSERT_PARTY = """
INSERT INTO PARTIDO (sigla, nomePartido)
VALUES ('{}', '{}');
"""


def create_insert_string(row):
    nome_partido = row[1]
    sigla_partido = row[2]

    insert_sql = INSERT_PARTY.format(
        sigla_partido,
        nome_partido
    )

    return insert_sql


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_partidos.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()


if __name__ == '__main__':
    filename = 'candidatura.csv'

    data = pd.read_csv(filename, usecols=['nome_partido', 'sigla_partido'])
    data = data.dropna(subset=['nome_partido', 'sigla_partido'])
    data = data.drop_duplicates(subset=['nome_partido', 'sigla_partido'])
    counter = 0
    lines = []
    for row in data.itertuples():
        line = create_insert_string(row)
        lines.append(line)

        counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
