import csv
import json


def parse_candidate(row):
    candidate = dict()
    candidate['cpf'] = row['cpf']
    candidate['nomeUrna'] = row['nome_urna']
    candidate['sexo'] = row['descricao_genero']
    candidate['nomeCandidato'] = row['nome']
    candidate['dtNascimento'] = row['data_nascimento']

    candidate['descricaoCargo'] = row['descricao_cargo']
    candidate['descricaoSituacao'] = row['descricao_situacao_candidatura']

    candidate['sigla'] = row['sigla_partido']
    candidate['nomePartido'] = row['nome_partido']

    candidate['ano'] = row['ano_eleicao']
    candidate['unidadeEleitoral'] = row['descricao_ue']
    candidate['unidadeFederativa'] = row['sigla_uf']
    candidate['descricaoResultado'] = row['descricao_totalizacao_turno']
    candidate['turno'] = row['numero_turno']

    return candidate


def validade_candidate(candidate):
    existing_fields = ['nomeCandidato', 'descricaoCargo', 'descricaoSituacao',
                       'sigla', 'ano', 'unidadeEleitoral',
                       'unidadeFederativa', 'descricaoResultado', 'turno']

    if int(candidate['cpf']) <= 0:
        return False
    else:
        for i in existing_fields:
            if not candidate[i]:
                return False

    return True


def read_csv(filename):
    counter = 0
    with open(filename, mode='r') as csvfile:
        readCSV = csv.DictReader(csvfile)

        with open('new_candidates.csv', mode='w') as new_csv_file:
            for row in readCSV:
                if counter == 0:
                    print(f'Column names = {", ".join(row)}')
                    counter += 1
                else:
                    candidate = parse_candidate(row)
                    if validade_candidate(candidate):
                        counter += 1

                        if counter <= 100:
                            print(json.dumps(candidate, indent=2))

    print('Total of valid rows = ', counter)


if __name__ == '__main__':
    read_csv('candidatura.csv')
