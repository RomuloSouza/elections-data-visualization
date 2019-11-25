import csv
import json

FIELD_NAMES = ['numeroSequencial', 'cpf']


def parse_sequencial_cpf(row):
    data = dict()
    data['numeroSequencial'] = row['numeroSequencial']
    data['cpf'] = row['cpf']

    return data


if __name__ == '__main__':

    counter = 0
    with open('new_candidates.csv', mode='r') as csvfile:
        readCSV = csv.DictReader(csvfile)

        with open('sequencial_cpf.csv', mode='w') as new_csv_file:
            writer = csv.DictWriter(new_csv_file, fieldnames=FIELD_NAMES)
            writer.writeheader()

            for row in readCSV:
                if counter == 0:
                    print(f'Column names = {", ".join(row)}')
                    counter += 1
                else:
                    data = parse_sequencial_cpf(row)
                    writer.writerow(data)
