import csv
import os

new_lst = []

with open('us_states.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        new_lst.append(row['ZIP code'])

print(new_lst)

BASIC_DIR = 'media/'

for code in new_lst:
    dirName = os.path.join(BASIC_DIR, code)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:
        print("Directory " , dirName ,  " already exists")

