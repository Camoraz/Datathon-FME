from rich import print

from participant import load_participants

participants = load_participants("./data/datathon_participants2.json")

print(participants[0])