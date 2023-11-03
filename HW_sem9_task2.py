func ='''
import csv
import json
from random import randint
import math

def save_to_json(func):
    def wrapper(file_name):
        with (open(f'{file_name}', 'r', newline='') as f_csv,
              open('results.json', 'w') as f_json):
            r = list(csv.reader(f_csv, delimiter=' ', quotechar='|'))
            roots = []
            for block in r:
                abc = list(map(int, block))
                roots.append(func(*abc))
            json.dump(roots, f_json)
    return wrapper


def generate_csv_file(file_name, rows):
    with open(f'{file_name}', 'w', newline='') as f_csv:
        w = csv.writer(f_csv, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for _ in range(rows):
            w.writerow([randint(100, 1000) for _ in range(3)])

@save_to_json
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        return [(-b + math.sqrt(discr)) / (2 * a),  (-b - math.sqrt(discr)) / (2 * a)]
    elif discr == 0:
        return [-b / (2 * a)]

'''

import os
current_path = os.getcwd()
with open(f'{current_path}/__init__.py', 'w', encoding='utf-8') as f:
    f.write(func)
