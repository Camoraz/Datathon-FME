from participant import load_participants
from rich import print
import numpy as np

data_path = "AEDChallenge/data/datathon_participants.json"
participants_pre = load_participants(data_path)

categorical = {
            "preferred_role":-2,
            "interest_in_challenges":5,
            "preferred_languages":5,
            "availability":10
            }

numeric = {"experience_level":1, "age":1, "year_of_study":1, "hackathons_done":0.5}
nlp = {"interests":1, "objective":5, }

def process_data(particips):
    year_mapping = {
    "1st year": 1,
    "2nd year": 2,
    "3rd year": 3,
    "4th year": 4,
    "Masters": 5,
    "PhD": 6
    }

    experience_map = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3
    }

    returning = particips

    for participant in returning:
        participant.year_of_study = year_mapping.get(participant.year_of_study, 0)  # Default to 0 if not found
        participant.experience_level = experience_map.get(participant.experience_level, 0)  # Default to 0 if not found
    return returning

def recommend(participant, n):

    participants = process_data(participants_pre)
    participant = process_data([participant])[0]

    # Compute normalizer
    norm = sum(categorical.values()) + sum(numeric.values()) + sum(nlp.values())

    distance_list = [0]*len(participants)
    effect_list = {}

    # Loop through all participants
    for i in range(len(participants)):

        # Initialize distance to 0
        distance = 0

        # Numeric - Euclidean Distance
        for variable, weight in numeric.items():
            change = abs(float(getattr(participant, variable))
                            - float(getattr(participants[i], variable))) * weight * norm
            distance += change
            effect_list[variable] = effect_list.get(variable, 0) + change
        
        # Categorical - Jaccard
        for variable, weight in categorical.items():
            change = int(getattr(participant, variable)
                            != getattr(participants[i], variable)) * weight * norm
            distance += change
            effect_list[variable] = effect_list.get(variable, 0) + change
        
        distance_list[i] = distance

    total_importance = sum(effect_list.values())

    for key in effect_list:
        effect_list[key] /= total_importance

    if n <= 0:
        return []
    
    return distance_list[:n], effect_list

distance, effect = recommend(participants_pre[15], 10)
print(effect)
