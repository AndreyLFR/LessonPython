items = {'ключи': 0.3,
         'кошелек': 0.2,
         'телефон': 0.5,
         'зажигалка': 0.1,
         }
max_weight = 1

def cycle_dict(tuple_thing, hoarder, max_weight):
    output_list = hoarder.copy()
    list_uniq_name = []

    for dict_ in hoarder:
        list_uniq_name.append(''.join(sorted(dict_.keys())))
        copy_dict = dict_.copy()
        copy_dict[tuple_thing[0]] = tuple_thing[1]
        if (sum(copy_dict.values()) <= max_weight) and (''.join(sorted(copy_dict.keys())) not in list_uniq_name):
            output_list.append(copy_dict)
    return output_list


result = [{thing: weight} for thing, weight in items.items() if weight <= max_weight]
for thing, weight in items.items():
    result = cycle_dict(tuple_thing=(thing, weight), hoarder=result, max_weight=max_weight)

print(result)