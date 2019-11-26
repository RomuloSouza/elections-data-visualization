import pandas as pd

INSERT_CANDIDATURA = """
INSERT INTO CANDIDATURA (cpf, ano, unidadeEleitoral, unidadeFederativa, idCargo, idSituacao, sigla)
VALUES ('{}', '{}', '{}', '{}', {}, {}, '{}');
"""

# INSERT INTO CANDIDATURA (cpf, ano, unidadeEleitoral, unidadeFederativa, idCargo, idSituacao, sigla)
# VALUES ('7857136204', 2000, 'ACRELANDIA', 'AC', 

# (select idCargo from CARGO where descricaoCargo = 'PREFEITO'), 
# (select idSituacao from SITUACAO where descricaoSituacao = 'alo'), 'PFL');

def create_insert_string(row):
    cpf = row[2]
    ano = row[11]
    unidadeEleitoral = row[12]
    unidadeFederativa = row[13]
    idCargo = f"(SELECT idCargo FROM CARGO WHERE descricaoCargo = '{row[7]}')"
    idSituacao = f"(SELECT idSituacao FROM SITUACAO WHERE descricaoSituacao = '{row[8]}')"
    sigla = row[9]

    insert_sql = INSERT_CANDIDATURA.format(
        cpf, ano, unidadeEleitoral, unidadeFederativa, idCargo, idSituacao,
        sigla
    )
    
    return insert_sql


def add_lines_to_file(lines):
    f = open('./sql_scripts/popula_candidatura.sql', 'w+')
    f.write('USE eleicoes;\n')
    for line in lines:
        f.write(line)

    f.close()

def read_cpfs():
    f = open('cpfs.txt', 'r')
    f = f.read().split('\n')

    return f


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

    data = pd.read_csv(filename, parse_dates=['dtNascimento'])
    counter = 0
    lines = []
    for row in data.itertuples():
        if binary_search(cpfs, str(row[2])):
            line = create_insert_string(row)
            lines.append(line)

            counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
