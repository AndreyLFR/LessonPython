date_to_prove = '31.6.2023'

def check_date(str):
    res = False
    day, mounth, year = str.split('.')
    date_dict = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30}
    date_dict[2] = 29 if int(year) % 4 == 0 else 28
    if int(mounth) in date_dict.keys() and 0 < int(day) < date_dict.get(int(mounth), 0):
        res = True
    return res

print(check_date(date_to_prove))