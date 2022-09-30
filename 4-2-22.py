import csv

with open('prices.csv', encoding='utf-8') as f:
    low_price = []
    for i in csv.DictReader(f, delimiter=';'):
        for k, v in i.items():
            if v.isdigit() and low_price == []:
                low_price = [[i['Магазин'], k, int(v)]]
            elif v.isdigit() and low_price[0][2] > int(v):
                low_price = [[i['Магазин'], k, int(v)]]
            elif v.isdigit() and low_price[0][2] == int(v):
                low_price.append([i['Магазин'], k, int(v)])
    print('{1}: {0}'.format(*sorted(sorted(low_price), key=lambda x: x[1])[0]))
