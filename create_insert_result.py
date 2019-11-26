import pandas as pd

INSERT_RESULT = """
INSERT INTO RESULTADO (descricaoResultado) VALUES ('{}');
"""


def create_insert_string(situacao):
    insert_sql = INSERT_RESULT.format(situacao)

    return insert_sql


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_resultado.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()


if __name__ == '__main__':
    filename = 'new_candidates.csv'

    data = pd.read_csv(filename, parse_dates=['dtNascimento'])
    counter = 0
    results = []
    for row in data.itertuples():
        results.append(row[14])

    lines = []
    for result in set(results):
        line = create_insert_string(result)
        lines.append(line)

        counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
