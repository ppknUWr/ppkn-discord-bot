import json

def read_reactions_roles_from_file():
    """
    read_reactions_roles_from_file
    Pozwala wczytać słownik z przypisanymi emotkami do roli z pliku

    @param -
    @return data: Dict - zawiera informacje odnośnie przypisanych ról do emotek
    """

    with open("data/reaction_roles.json", "r") as f:
        data = json.load(f)
        return data