
def write_file_w(path):
    with open(path, 'w') as file:
        file.write(input("Ведите текст: "))

def read_file_r(path):
    with open(path,'r') as file:
        return file.read()

def write_file(path, text):
    with open(path, 'w') as file:
        file.write(text)
