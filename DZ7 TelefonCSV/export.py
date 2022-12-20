import csv

def export_str(str_exp):
    with open('direct.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if str_exp[0] in row and str_exp[1] in row:
                return row