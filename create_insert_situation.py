import pandas as pd

INSERT_SITUATION = """
INSERT INTO SITUACAO (descricaoSituacao) VALUES ('{}');
"""


def create_insert_string(situacao):
    insert_sql = INSERT_SITUATION.format(situacao)
    
    return insert_sql


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_situacao.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()


if __name__ == '__main__':
    filename = 'new_candidates.csv'

    data = pd.read_csv(filename, parse_dates=['dtNascimento'])
    counter = 0
    situations = []
    for row in data.itertuples():
        situations.append(row[8])
    
    lines = []
    for situation in set(situations):
        line = create_insert_string(situation)
        lines.append(line)

        counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
