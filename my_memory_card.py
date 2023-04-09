from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle


class Question ():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []
question_list.append(Question('Какого цвет нет на лого алгоритмики', 'зелёный', 'жёлтый', 'фиолетовый', 'белый'))
question_list.append(Question('Какой год называют "Милениум"', '2000', '1999', '2001', '2222'))
question_list.append(Question('Как переводится "Ряд" на английский язык?', 'row', 'raid', 'road', 'rail'))

shuffle(question_list)

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox("Варианты ответов")
rdtn_1 = QRadioButton('Энцы')
rdtn_2 = QRadioButton('Смурфы')
rdtn_3 = QRadioButton('Чулымцы')
rdtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rdtn_1)
RadioGroup.addButton(rdtn_2)
RadioGroup.addButton(rdtn_3)
RadioGroup.addButton(rdtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rdtn_1)
layout_ans2.addWidget(rdtn_2)
layout_ans3.addWidget(rdtn_3)
layout_ans3.addWidget(rdtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnswerGroup = QGroupBox('Результат теста')
lb_result = QLabel(' правильно/неправильно')
lb_current = QLabel(' Правильный ответ')
answer_line = QVBoxLayout()

answer_line.addWidget(lb_result)
answer_line.addWidget(lb_current)

AnswerGroup.setLayout(answer_line)

layout_ans = QVBoxLayout()
layout_ans.addWidget(question)
layout_ans.addWidget(RadioGroupBox)
layout_ans.addWidget(AnswerGroup)
AnswerGroup.hide()
btn_OK = QPushButton('Ответить')
def show_result():
    RadioGroupBox.hide()
    AnswerGroup.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroup.setExclusive(False)
    rdtn_1.setChecked(False)
    rdtn_2.setChecked(False)
    rdtn_3.setChecked(False)
    rdtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnswerGroup.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')

def start():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answers = [rdtn_1, rdtn_2, rdtn_3, rdtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    question.setText(q.question)
    lb_current.setText(q.right_answer)
    show_question()

def next_question():
    main_win.num_of_question += 1
    if main_win.num_of_question == len(question_list):
        main_win.num_of_question = 0
    q = question_list[main_win.num_of_question]
    ask(q)

def check_answer():
    if answers[0].isChecked() == True:
        lb_result.setText('Правильно!')
    else:
        lb_result.setText('Неверно!')
    show_result()

main_win.num_of_question = -1
next_question()
btn_OK.clicked.connect(start)

layout_ans.addWidget(btn_OK)

main_win.setLayout(layout_ans)
main_win.show()
app.exec_()