import pandas as pd

MAX_CANDIDATES = 15

INSERT_CANDIDATE = """
INSERT INTO CANDIDATO (cpf, nomeUrna, sexo, nomeCandidato, dtNascimento)
VALUES ('{}', '{}', '{}', '{}', '{}');
"""


def create_insert_string(row):
    dt = str(row[6])
    dt = f'{dt[-4:]}-{dt[2:4]}-{dt[0:2]}'

    insert_sql = INSERT_CANDIDATE.format(
        row[2],
        row[3],
        row[4],
        row[5],
        dt
    )
    
    return insert_sql


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
    for row in data.itertuples():
        if counter < MAX_CANDIDATES:
            line = create_insert_string(row)
            lines.append(line)
        else:
            break

        counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
