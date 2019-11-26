import pandas as pd

INSERT_CANDIDATE = """
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

    insert_sql = INSERT_CANDIDATE.format(
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


if __name__ == '__main__':
    filename = 'new_candidates.csv'

    data = pd.read_csv(filename, parse_dates=['dtNascimento'])
    counter = 0
    lines = []
    for row in data.itertuples():
        line = create_insert_string(row)
        lines.append(line)

        counter += 1

    print('tamanho = ', counter)
    add_lines_to_file(lines)
