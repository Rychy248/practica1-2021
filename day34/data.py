import requests
import random

params = {
    'amount':10,
    'category':18, #computer science
    'type':"boolean",
    #'difficulty':f"{random.choice(['easy','medium','hard'])}",
}
response = requests.get(url="https://opentdb.com/api.php?",params=params)
data = response.json()
question_data = data['results']

#format resulted
# question_data = [
#    {
#        "category": "Science: Computers",
#        "type": "boolean",
#        "difficulty": "medium",
#        "question": "The HTML5 standard was published in 2014.",
#        "correct_answer": "True",
#        "incorrect_answers": [
#            "False"
#        ]
#    },
#]