# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from itertools import count
import func_files

path = 'file2.txt'
path_total = 'file2_rle'

func_files.write_file_w(path)
text = func_files.read_file_r(path)

unic_symbol = set(text)
print(unic_symbol)

dict_amount_symbol = []
for i in unic_symbol:
    count = 0
    for j in text:
        if i == j:
            count += 1
    dict_amount_symbol.append(i)
    dict_amount_symbol.append(f'{count}')
text_rle = ''.join(dict_amount_symbol)

func_files.write_file(path_total, text_rle)
