from pathlib import Path
import json
import os.path

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

def save_to_file(file, dictionary):#zapisze dane do pliku json
    if (os.path.isfile("API_data/"+file) == True and os.path.getsize(file) != 0):
        with open("API_data/"+file, "r+") as f:
            data = json.load(f)
            data.update(dictionary)
            f.seek(0)
            json.dump(data, f)
    else:
        with open("API_data/"+file, "w") as f:
            json.dump(dictionary, f)
