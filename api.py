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
    
    form = FormData(data['years'], data['role'], data['challenge'], data['lang'], data['level'], data['age'], data['hackathons'])
    print(form.years, form.role, form.challenge, form.lang, form.level, form.age, form.hackathons)
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
                              objective='i want to be happy',
                              objective_vector=None,
                              interest_in_challenges=form.challenge,
                              preferred_languages=form.lang,
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
    


    _, response = recommend(participant, 5)

    return jsonify({"message": "Received", "data": _})

if __name__ == '__main__':
    app.run(debug=True)
