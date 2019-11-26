import pandas as pd

INSERT_JOB = """
INSERT INTO CARGO (descricaoCargo) VALUES ('{}');
"""


def create_insert_string(job):
    insert_sql = INSERT_JOB.format(job)

    return insert_sql


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_cargos.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()


if __name__ == '__main__':
    filename = 'new_candidates.csv'

    data = pd.read_csv(filename, parse_dates=['dtNascimento'])
    counter = 0
    jobs = []
    for row in data.itertuples():
        jobs.append(row[7])

    lines = []
    for job in set(jobs):
        line = create_insert_string(job)
        lines.append(line)

        counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
