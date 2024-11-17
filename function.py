import json
from participant import load_participants
from rich import print
import numpy as np
from sentence_transformers import SentenceTransformer, util
import re

# Load the pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to get sentence embeddings
def get_sentence_embedding(sentence, model):
    # Function to detect negation words and adjust the sentence's polarity using regex
    def handle_negation(sentence):
        # Define a pattern to look for negation words
        negation_pattern = r"\b(?:not|never|no|n't|without|hardly|barely|nothing)\b"
        
        # Search for negations in the sentence
        if re.search(negation_pattern, sentence.lower()):
            # Flip the sentiment (simplified approach)
            sentence = re.sub(negation_pattern, 'NEGATED', sentence, flags=re.IGNORECASE)
        
        return sentence

    # Handle negations before generating embedding
    adjusted_sentence = handle_negation(sentence)
    embedding = model.encode(adjusted_sentence, convert_to_tensor=True)
    return embedding

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

def load_data():
    data_path = "./data/datathon_participants2.json"
    participants = load_participants(data_path)
    participants = process_data(participants)
    data_types = {
        "categorical" : {
                        "preferred_role":-2,
                        "interest_in_challenges":5,
                        "preferred_languages":5,
                        "availability":10,
                        "programming_skills":-3
                        },
        "numeric" : {"experience_level":1, "preferred_team_size":1,
                     "age":1, "year_of_study":1, "hackathons_done":0.5},
        "nlp" : {"objective_vector":5}
    }

    return participants, data_types


def recommend(participant, n):
    print('recommending')
    participants, data_types = load_data()

    categorical = data_types["categorical"]
    numeric = data_types["numeric"]
    nlp = data_types["nlp"]

    participant = process_data([participant])[0]

    participant.objective_vector = get_sentence_embedding(participant.objective, model)

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

        for variable, weight in nlp.items():
            change = (1 - util.pytorch_cos_sim(getattr(participant, variable),
                                            getattr(participants[i], variable)).item() ** 2) * weight * norm
            distance += change
            effect_list[variable] = effect_list.get(variable, 0) + change

        distance_list[i] = (distance, participants[i].id)

    total_importance = sum(effect_list.values())

    for key in effect_list:
        effect_list[key] /= total_importance

    if n <= 0:
        return []
    
    distance_list.sort(key=lambda x: x[0])
    maxim = max(max(distance_list, key=lambda x: x[0])[0], 2000)
    return [(distance_list[i][1],round( 100 - (distance_list[i][0] / maxim) * 100), 2) for i in range(n)], effect_list


if __name__ == '__main__':
    
    from participant import Participant
    
    participant = Participant(id="shuwe78wasd",
                              name="Raúl",
                              email=None,
                              age=18,
                              year_of_study="4th year",
                              shirt_size=None,
                              university=None,
                              dietary_restrictions=None,
                              programming_skills={
            "C#": 2,
            "C++": 4,
            "C": 6,
            "Unity": 3,
            "Python": 3,
            "JavaScript": 2,
            "NodeJS": 5,
            "Numpy": 2,
            "SQL": 5
        },
                              experience_level="Intermediate",
                              hackathons_done=2,
                              interests=None,
                              preferred_role=["Design"],
                              objective="I'm super stoked to be participating in this datathon! My goal is to soak up the vibes, learn from others, and have an absolute blast. I want to join in on as many events and workshops as I can, learn new skills and insights, and make friends with like-minded peeps. I'm more about having fun and making connections than about trying to win (although, I do love a good challenge!). My objective is to leave this datathon feeling refreshed, inspired, and with new friendships to look back on. Bring it on!",
                              objective_vector=None,
                              interest_in_challenges=["restb.ai"],
                              preferred_languages=["English", "Catalan"],
                              friend_registration=[],
                              preferred_team_size=4,
                              availability= {"Saturday morning": True,
                                        "Saturday afternoon": True,
                                        "Saturday night": False,
                                        "Sunday morning": True,
                                        "Sunday afternoon": True },
                              introduction=None,
                              technical_project=None,
                              future_excitement=None,
                              fun_fact=None)

    distance, effect = recommend(participant, 10)
    print(distance)