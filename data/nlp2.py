from sentence_transformers import SentenceTransformer, util
import re

# Load the pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to detect negation words and adjust the sentence's polarity using regex
def handle_negation(sentence):
    # Define a pattern to look for negation words
    negation_pattern = r"\b(?:not|never|no|n't|without|hardly|barely|nothing)\b"
    
    # Search for negations in the sentence
    if re.search(negation_pattern, sentence.lower()):
        # Flip the sentiment (simplified approach)
        sentence = re.sub(negation_pattern, 'NEGATED', sentence, flags=re.IGNORECASE)
    
    return sentence

# Function to get sentence embeddings
def get_sentence_embedding(sentence, model):
    # Handle negations before generating embedding
    adjusted_sentence = handle_negation(sentence)
    embedding = model.encode(adjusted_sentence, convert_to_tensor=True)
    return embedding

# Function to compute cosine similarity between two sentences
def compute_similarity(sentence1, sentence2, model):
    # Get embeddings for both sentences
    embedding1 = get_sentence_embedding(sentence1, model)
    embedding2 = get_sentence_embedding(sentence2, model)
    
    # Compute cosine similarity
    similarity = util.pytorch_cos_sim(embedding1, embedding2)
    return similarity.item()