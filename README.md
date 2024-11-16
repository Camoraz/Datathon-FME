<div align="center">
    <img src="public/aed_logo.png" width="200" alt="AED logo" />
    <h1>Repte AED - Datathon FME 2024</h1>
</div>

## Documentation

### Participant

The `Participant` class is a dataclass that represents a participant in the datathon. It contains all the information about a participant, including their personal data, experience and skills, interests, preferences and constraints.

1. `id`: A unique identifier for the participant. This is automatically generated when the participant is created.
2. `name`: The name of the participant. It may contain [Non-ASCII characters](https://blog.jpalardy.com/posts/dealing-with-non-ascii-characters/)
3. `email`: The email of the participant.
4. `age`: The age of the participant.
5. `year_of_study`: The year of study of the participant. It can be one of the following: "1st year", "2nd year", "3rd year", "4th year", "Masters", "PhD".
6. `shirt_size`: The shirt size of the participant. It can be one of the following: "S", "M", "L", "XL".
7. `university`: The university of the participant.
8. `dietary_restrictions`: The dietary restrictions of the participant. It can be one of the following: "None", "Vegetarian", "Vegan", "Gluten-free", "Other".
9. `programming_skills`: The programming skills of the participant. It is a dictionary with programming languages or tools as keys and integers as values. The integers represent the skill level, which can be one of the following: 1, 2, 3, 4, 5.
10. `experience_level`: The experience level of the participant. It can be one of the following: "Beginner", "Intermediate", "Advanced".
11. `hackathons_done`: The number of hackathons done by the participant.
12. `interests`: The interests of the participant. It is a list of strings, each string representing an interest. 
13. `preferred_role`: The preferred role of the participant. It can be one of the following: "Analysis", "Visualization", "Development", "Design".
14. `objective`: The objective of the participant. This is a response to the a free-form question "What are you looking for at Datathon FME 2024?". The response is usually related to one of: "prize-hunting", "portfolio-building", "learning new skills", "meeting new people".
15. `interest_in_challenges`: The interest in challenges of the participant. It is a list of strings, each string representing a challenge. 
16. `preferred_languages`: The preferred languages of the participant. It is a list of strings, each string representing a programming language.
17. `friend_registration`: The list of friends of the participant. It is a list of UUIDs, each UUID representing a participant.
18. `preferred_team_size`: The preferred team size of the participant. It is an integer between 1 and 5.
19. `availability`: The availability of the participant. It is a dictionary with days and times as keys and boolean values as values.
20. `introduction`: The introduction of the participant. This is a response to the free-form question "Tell us about yourself".
21. `technical_project`: The technical project of the participant. This is a response to the free-form question "Tell us about a project you’ve enjoyed working on, technical or non-technical.".
22. `future_excitement`: The future excitement of the participant. This is a response to the free-form question "What’s something you’re excited to work on in the next 10 years? Dream big!".
23. `fun_fact`: The fun fact of the participant. This is a response to the free-form question "Tell us a fun fact about you :".
