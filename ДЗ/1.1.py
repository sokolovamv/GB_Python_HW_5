# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import func_files

func_files.write_file_w()
text = func_files.read_file_r()

print(' '.join([i for i in text if 'абв' not in i]))