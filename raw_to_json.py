import codecs
import json
import re


class Question:
    def __init__(self):
        self.qid = None
        self.answer = ""
        self.question = ""
        self.options = {}


def get_lines():
    with codecs.open('raw.txt', "rb", "utf-8") as rawf:
        return [line.strip() for line in rawf]


inquestion = False
questions = []
FIRST_LINE_RE = re.compile(r'(T\d[A-F]\d\d) \(([A-D])\)')

for line in get_lines():
    first_line_match = FIRST_LINE_RE.match(line)

    if first_line_match is not None:
        inquestion = True
        curq = Question()
        curq.qid, curq.answer = first_line_match.groups()
    elif inquestion and line.startswith(('A. ', 'B. ', 'C. ', 'D. ')):
        letter = line[0:1]
        curq.options[letter] = line[3:]
    elif inquestion and line == '~~':
        inquestion = False
        questions.append(curq)
    elif inquestion:
        curq.question = line

print(json.dumps([q.__dict__ for q in questions]))
