from pathlib import Path
import json
import os.path

"""
TODO: Dokumentacja
"""
def read_all_files():#wczyta wszystkie pliki
    paths = Path('api_data').glob('*.*')
    for path in paths:
        path_in_str = str(path)#konwersja z objektu na string
        with open(path_in_str) as f:
            print(f.read())
    return True

"""
TODO: Dokumentacja
"""
def read_file(file):#wczyta podany plik i zwroci dane w postaci slownika
    if os.path.isfile(file):
        with open("api_data/"+file, "r") as f:
            try:
                dictionary = json.load(f)
                f.close()
                return dictionary
            except:
                print("Wrong file extension (should be .json) or empty file!\n")
                return None
    else:
        print("File doesnt exist!\n")
        return None

"""
TODO: Dokumentacja
"""
def save_to_file(file, dictionary):#zapisze dane do pliku json
    if (os.path.isfile("api_data/"+file) == True and os.path.getsize(file) != 0):
        with open("API_data/"+file, "r+") as f:
            data = json.load(f)
            data.update(dictionary)
            f.seek(0)
            json.dump(data, f)
    else:
        with open("API_data/"+file, "w") as f:
            json.dump(dictionary, f)
