from pathlib import Path

def read_all_files():#wczyta wszystkie pliki
    paths = Path('API_data').glob('*.*')
    for path in paths:
        path_in_str = str(path)#konwersja z objektu na string
        f=open(path_in_str,"r")
        print(f.read())
        f.close()
    return True
#read_all_files()

def read_file(file):#wczyta podany plik
    f=open("API_data/"+file,"r")
    print(f.read())
    f.close()
    return True
read_file("test.txt")

