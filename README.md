<div align="center">
    <img src="public/aed_logo.png" width="200" alt="AED logo" />
    <h1>Repte AED - Datathon FME 2024</h1>
</div>

# Participant Recommendation System

This Python project implements a recommendation system for participants in a datathon. It matches participants based on their attributes, interests, and goals using a combination of numerical, categorical, and natural language features.

# Features
## Preprocessing:

Maps attributes like academic year and experience level to numeric values.
Encodes participant objectives into semantic vectors using a pre-trained Sentence-BERT model (all-MiniLM-L6-v2).
Handles negation in sentences to improve embeddings.

# Measures similarity using:
 - *Numerical features*: Euclidean distance.
 - *Categorical features*: Jaccard distance.
 - *NLP features*: Cosine similarity of sentence embeddings.
Weights features dynamically to compute a comprehensive similarity score.

# Recommendations:

Suggests the top n most similar participants to a given participant, according to how many people you need for your team.

Provides insights into the relative importance of each feature in the recommendation process.
