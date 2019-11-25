import csv

FIELD_NAMES = ['numeroSequencial', 'ano', 'detalhe', 'valor',
               'descricaoTipoPatrimonio']


def parse_material_goods(row):
    item = dict()
    item['numeroSequencial'] = row['numero_sequencial']
    item['ano'] = row['ano_eleicao']
    item['detalhe'] = row['detalhe']
    item['descricaoTipoPatrimonio'] = row['descricao_tipo']
    item['valor'] = row['valor']

    return item


def validate_goods(item):
    existing_fields = ['numeroSequencial', 'ano', 'detalhe', 'valor',
                       'descricaoTipoPatrimonio']

    if float(item['valor']) <= 0:
        return False
    else:
        for i in existing_fields:
            if not item[i]:
                return False

    return True


if __name__ == '__main__':
    counter = 0
    invalid = 0
    with open('bem-declarado.csv', mode='r') as csvfile:
        readCSV = csv.DictReader(csvfile)

        with open('new_material_goods.csv', mode='w') as new_csv_file:
            writer = csv.DictWriter(new_csv_file, fieldnames=FIELD_NAMES)
            writer.writeheader()

            for row in readCSV:
                if counter == 0:
                    print(f'Column names = {", ".join(row)}')
                    counter += 1
                else:
                    item = parse_material_goods(row)
                    if validate_goods(item):
                        writer.writerow(item)
                        counter += 1
                    else:
                        invalid += 1

    print('Total of valid rows = ', counter)
    print('Total of invalid rows = ', invalid)
