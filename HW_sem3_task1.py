import random

backpack = {}
items = {'ключи': 0.3,
         'кошелек': 0.2,
         'телефон': 0.5,
         'зажигалка': 0.1,
         }
max_weight = 1

thing_list = list(items.keys())
random.shuffle(thing_list)

for thing in thing_list:
    if sum(backpack.values()) + items[thing] <= max_weight:
        backpack[thing] = items[thing]

print(backpack)