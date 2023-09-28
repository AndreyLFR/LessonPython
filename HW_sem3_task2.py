from typing import List

text = 'Hello world. Hello Python. Hello again.'
list_marks = ['.', ',', ':', ';', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for mark in list_marks:
    text = text.replace(mark, '')

words_list: list[str] = text.lower().split()

output_list = [(word, words_list.count(word)) for word in set(words_list)]
output_list.sort(key=lambda a: a[1], reverse=True)
output_list = output_list[:10]
print(output_list)