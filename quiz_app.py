import json
from flask import Flask, request
from flask import render_template,flash

from models import Question

app = Flask(__name__)
# Reading question bank file to select a file.
@app.route("/") 
def index():
    with open('data/question_bank.json', 'rb') as choose_quiz:
        quiz_bank = json.load(choose_quiz)
#rendering page for file selection.
    return render_template("question_bank.html", quiz_bank=quiz_bank) 


# Reading Question paper file using a class.
@app.route("/takequiz/<quiz_name>/")
def takeQuiz(quiz_name):
    filename = 'data/' + quiz_name + '.json'
    question = Question(filename) 
    return render_template("take_quiz.html",quiz = question.quiz, quiz_name=quiz_name)
           
#Receiving same file to check answers and calculate score.
@app.route("/answer/<quiz_name>/", methods =['POST'])
def answer(quiz_name):
    filename = 'data/' + quiz_name + '.json'
    question = Question(filename)
    check = [] # list of tuples - original questions and user given answers.
    score = 0   
    for option in request.form:
        q_num = int(option.split('-')[-1])
        ans_given = request.form.get(option)
        result = question.check(q_num, ans_given)# calling class method to check answers.
        if result:
            score += 1
    return render_template("result.html" ,score = score) #user can see score in result.html


if __name__ == '__main__':
    app.run(debug = True)
"""
@app.route("/create")
def create():
    return render_template("create_page.html")


@app.route("/addquestion")
def up_date():
    return render_template("add_question.html")
"""
