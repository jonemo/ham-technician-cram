import json
import random


class Question:
    def __init__(self, qid, answer, question, options):
        self.qid = qid
        self.answer = answer
        self.question = question
        self.options = options

    def printit(self, idx, length):
        print(f"Question {self.qid} ({idx}/{length}):")
        print('---')
        print(self.question)
        print('---')
        for letter in ['A', 'B', 'C', 'D']:
            print(f"{letter}: {self.options[letter]}")
        print('---')


with open('quespool.json') as inf:
    unshuffled_list = json.load(inf)

shuffled_list = random.sample(unshuffled_list, k=len(unshuffled_list))

for idx, q in enumerate(shuffled_list):
    question = Question(
        qid=q['qid'],
        question=q['question'],
        answer=q['answer'],
        options=q['options'],
    )

    # Put filters for questions you don't want to see here. For example:
    # if question.question.startswith("What is the resistance") or \
    #         question.question.startswith("What is the voltage") or \
    #         question.question.startswith("What is the current"):
    #     continue

    question.printit(idx=idx+1, length=len(shuffled_list))
    response = input("? ").upper()
    if response == question.answer:
        print('correct')
    else:
        print(f"wrong ({question.answer})")
        with open('quespool-wrong.txt', 'a') as respf:
            respf.write(f"{question.qid} {question.question}\n")
    print('===')
    print()
