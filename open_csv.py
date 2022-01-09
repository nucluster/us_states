import csv

new_lst = []

with open('us_states.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
