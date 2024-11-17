from flask import Flask, request, jsonify
from flask_cors import CORS
from format_data import FormData
from function import recommend
from participant import Participant

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # Permite solo desde React

@app.route('/api', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    
    form = FormData(data['years'], data['role'], data['challenge'], data['lang'], data['level'], data['age'], data['hackathons'], data["availability"], data["objective"])
    print(form.years, form.role, form.challenge, form.lang, form.level, form.age, form.hackathons, form.availability)
    participant = Participant(id=None,
                              name=None,
                              email=None,
                              age=form.age,
                              year_of_study=form.years,
                              shirt_size=None,
                              university=None,
                              dietary_restrictions=None,
                              programming_skills=None,
                              experience_level=form.level,
                              hackathons_done=form.hackathons,
                              interests=None,
                              preferred_role=form.role,
                              objective=form.objective,
                              objective_vector=None,
                              interest_in_challenges=form.challenge,
                              preferred_languages=form.lang,
                              friend_registration=[],
                              preferred_team_size=4,
                              availability= form.availability,
                              introduction=None,
                              technical_project=None,
                              future_excitement=None,
                              fun_fact=None)
    


    people = recommend(participant, 5)[0]
    print(people)
    people_dict = {}
    for person in people:
        print(person)
        people_dict[person[0]] = person[1]

    return jsonify({"message": "Received", "data": people_dict})

if __name__ == '__main__':
    app.run(debug=True)
