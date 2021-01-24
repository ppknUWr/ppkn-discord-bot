import json


"""
save_meeting_to_file
Pozwala zapisac spotkanie do pliku .json

@param meeting: Dict - zawiera pola odnosnie inforamcji o spotkaniu, jak data i nazwa spotkania
@return -
"""
def save_meeting_to_file(meeting):
    with open("data/meetings.json", "r+") as f:
        data = json.load(f)
        data.append(meeting)
        f.seek(0)
        json.dump(data, f)
        print("Done")


def read_meetings_from_file():
    with open("data/meetings.json", "r") as f:
        data = json.load(f)
        return data

# def read_meetings_from_file():
#     with open("data/meetings.json", "r") as f:
#         try:
#             dictionary = json.load(f)
#             f.close()
#             return dictionary