func = '''import json
import csv
import os
import pickle


def folder_size(path='.'):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    return total

def save_results_to_json(key_, add_data):
    if os.path.exists('HW8.json'):
        with open('HW8.json', 'r', encoding='utf-8') as f_json:
            data = json.load(f_json)
            data[key_] = data[key_] + add_data if key_ in data else add_data
    else:
        data = {key_: add_data}
    with open('HW8.json', 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, indent=2)

def save_results_to_csv(key_, add_data):
    mode = 'a' if os.path.exists('HW8.csv') else 'w'
    with open('HW8.csv', mode, newline='') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=['name', 'type', 'size', '.'], delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if mode == 'w':
            writer.writeheader()
        for dict_ in add_data:
            dict_['.'] = key_
            writer.writerow(dict_)

def save_results_to_pickle(key_, add_data):
    mode = 'ab' if os.path.exists('HW8.pickle') else 'wb'
    with open('HW8.pickle', mode) as f_pickle:
        for dict_ in add_data:
            dict_['.'] = key_
            pickle.dump(dict_, f_pickle)

def traverse_directory(catalog):
    for root, dirs, files in os.walk(catalog):
        blocks_dir = [{'name': catalog.split('/')[-1], 'type': 'directory', 'size': folder_size(root)}] + \
                     [{'name': f, 'type': 'file', 'size': os.stat(catalog).st_size} for f in files]
        save_results_to_json(key_=catalog.split('/')[-1], add_data=blocks_dir)
        save_results_to_csv(key_=catalog.split('/')[-1], add_data=blocks_dir)
        save_results_to_pickle(key_=catalog.split('/')[-1], add_data=blocks_dir)
        if dirs:
            [traverse_directory(f'{catalog}/{d}') for d in dirs]

'''
import os
current_path = os.getcwd()
with open(f'{current_path}/__init__.py', 'w', encoding='utf-8') as f:
    f.write(func)
