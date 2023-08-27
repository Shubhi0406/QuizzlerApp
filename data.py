import requests

# Describes the type of questions to be picked
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}


# gets random questions from a trivia database https://opentdb.com/api.php
def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]


# assigns the questions to a variable
question_data = get_questions()
