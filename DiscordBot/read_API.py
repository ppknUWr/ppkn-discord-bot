from pathlib import Path

def read_all_files():#wczyta wszystkie pliki
    paths = Path('API_data').glob('*.*')
    for path in paths:
        path_in_str = str(path)#konwersja z objektu na string
        with open(path_in_str) as f:
            print(f.read())
    return True
read_all_files()

def read_file(file):#wczyta podany plik
    with open("API_data/"+file) as f:
        print(f.read())
    return True
read_file("test.txt")

