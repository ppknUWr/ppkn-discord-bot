import json


def save_meeting_to_file(meeting):
    """
    save_meeting_to_file
    Pozwala zapisac spotkanie do pliku .json

    @param meeting: Dict - zawiera pola odnosnie inforamcji o spotkaniu, jak data i nazwa spotkania
    @return -
    """

    with open("data/meetings.json", "r+") as f:
        data = json.load(f)
        data.append(meeting)
        f.seek(0)
        json.dump(data, f)
        print("Done")


def save_all_meetings(meetings):
    """
    save_all_meetings
    Pozwala NADPISAC przekazanym slownikiem zawartosc pliku .json

    @param meetings: List[Dict] - lista, zawierająca słowniki z danymi odnośnie spotkań
    @return -
    """

    with open("data/meetings.json", "w") as f:
        f.truncate(0)
        json.dump(meetings, f)

def read_meetings_from_file():
    """
    read_meetings_from_file
    Pozwala wczytać spotkania z pliku

    @param -
    @return data: List[Dict] - zawiera pola odnosnie inforamcji o spotkaniu, jak data i nazwa spotkania
    """

    with open("data/meetings.json", "r") as f:
        data = json.load(f)
        return data