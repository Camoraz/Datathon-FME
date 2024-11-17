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
    data_path = "./AEDChallenge/data/datathon_participants2.json"
    participants = load_participants(data_path)
    participants = process_data(participants)
    data_types = {
        "categorical" : {
                        "preferred_role":-2,
                        "interest_in_challenges":5,
                        "preferred_languages":5,
                        "availability":10
                        },
        "numeric" : {"experience_level":1, "age":1, "year_of_study":1, "hackathons_done":0.5},
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

        distance_list[i] = distance

    total_importance = sum(effect_list.values())

    for key in effect_list:
        effect_list[key] /= total_importance

    if n <= 0:
        return []
    
    return distance_list[:n], effect_list


if __name__ == '__main__':
    
    from participant import Participant
    
    participant = Participant(id=None,
                              name=None,
                              email=None,
                              age=2,
                              year_of_study=4,
                              shirt_size=None,
                              university=None,
                              dietary_restrictions=None,
                              programming_skills=["Python"],
                              experience_level="Beginner",
                              hackathons_done=5,
                              interests=None,
                              preferred_role=["Analysis"],
                              objective="Hello, I want to win",
                              objective_vector=None,
                              interest_in_challenges=["restb.ai"],
                              preferred_languages=["spanish"],
                              friend_registration=None,
                              preferred_team_size=None,
                              availability= {"Saturday morning": False,
                                        "Saturday afternoon": True,
                                        "Saturday night": True,
                                        "Sunday morning": True,
                                        "Sunday afternoon": True },
                              introduction=None,
                              technical_project=None,
                              future_excitement=None,
                              fun_fact=None)

    distance, effect = recommend(participant, 10)
    print(effect)
