import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        result = {}
        for i in reader:
            for j in i:
                result.setdefault(j, []).append(i[j])
    return result


print(csv_columns('deniro.csv'))
