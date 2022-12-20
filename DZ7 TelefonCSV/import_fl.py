import csv
def import_csv(str_imp):
    with open('direct.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(str_imp)