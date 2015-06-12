import json

# class Question reads a file and holds a list object
class Question(object):

    def __init__(self, filename):
        self.quiz = []
        with open(filename, 'rb') as quiz_file:
            self.quiz = json.load(quiz_file)

    def check(self, q_num, ans_given): # method to check answers.
        question = self.quiz[q_num]
        if question['ans'] == ans_given:
            return True
        return False
