#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
 
from random import shuffle , randint

class Question:
    def __init__(self,text,right_answer,wrong1,wrong2,wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("На якій планеті ми живемо?", "Земля","Юпітер","Марс","Сатурн"))
question_list.append(Question("Яку планету називають Червоною планетою?", "Марс","Нептун","Уран","Венера"))
question_list.append(Question("Яка планета найбільша в Сонячній системі?", "Юпітер","Земля","Нептун","Сатурн"))
question_list.append(Question("Скільки планет у Сонячній системі?", "8","6","10","9"))

app = QApplication([]) 
window = QWidget()
window.resize(400, 200) 
window.setWindowTitle("Memory Card")

question = QLabel("Яка планета найближча до Сонця?")
answer1 = QRadioButton("Меркурій")
answer2 = QRadioButton("Марс")
answer3 = QRadioButton("Земля")
answer4 = QRadioButton("Венера")
GroupBox = QGroupBox("Відповіді")
Button = QPushButton("Відповідь")

RG = QButtonGroup()
RG.addButton(answer1)
RG.addButton(answer2)
RG.addButton(answer3)
RG.addButton(answer4)

RGB = QGroupBox("Result")
Result = QLabel("тут буде результат",alignment=Qt.AlignCenter)
Correct = QLabel("тут буде правильна відповідь", alignment=Qt.AlignCenter)
RLV1 = QVBoxLayout()
RLV1.addWidget(Result, alignment=Qt.AlignCenter)
RLV1.addWidget(Correct, alignment=Qt.AlignCenter)
RGB.setLayout(RLV1)
RGB.hide()



lineH1 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineV1.addWidget(answer1, alignment=Qt.AlignCenter)
lineV1.addWidget(answer2, alignment=Qt.AlignCenter)
lineV2.addWidget(answer3, alignment=Qt.AlignCenter)
lineV2.addWidget(answer4, alignment=Qt.AlignCenter)


lineH1.addLayout(lineV1)
lineH1.addLayout(lineV2)
GroupBox.setLayout(lineH1)

main_lineH1 = QHBoxLayout()
main_lineH2 = QHBoxLayout()
main_lineH3 = QHBoxLayout()

main_lineH1.addWidget(question, alignment=Qt.AlignCenter)
main_lineH2.addWidget(GroupBox, alignment=Qt.AlignCenter)
main_lineH3.addWidget(Button, alignment=Qt.AlignCenter)
main_lineH2.addWidget(RGB, alignment=Qt.AlignCenter)

main_lineV1 = QVBoxLayout()
main_lineV1.addLayout(main_lineH1,stretch=2)
main_lineV1.addStretch(1)
main_lineV1.addLayout(main_lineH2,stretch=8)
main_lineV1.addLayout(main_lineH3,stretch=1)
main_lineV1.setSpacing(5)

window.setLayout(main_lineV1)
def Show_Result(): 
    GroupBox.hide()
    RGB.show()
    Button.setText("Наступне запитання")

def Show_Qestion():
    GroupBox.show()
    RGB.hide()
    RG.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    
    RG.setExclusive(True)

answers = [answer1 , answer2, answer3 , answer4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.text)
    Correct.setText("Правильна відповідь"+ q.right_answer)
    Show_Qestion()

def right_wrong():
    window.total += 1
    if RG.checkedButton() is None:
        return
    if answers[0].isChecked():
        Result.setText('Правильно')
        window.score += 1
    else:
        Result.setText("Неправильно")
    Show_Result()
    rating = window.score/window.total * 100
    print("Дано відповідей:",window.total)
    print("Правильні відповіді:",window.score)
    print("Успех:",rating,"%")
def next_question():
    random_question = randint(0,len(question_list)-1)
    q = question_list[random_question]
    ask(q)
def button_OK():
    if Button.text() == "Відповідь":
        right_wrong()
    else:
        next_question()

Button.clicked.connect(button_OK)
window.score = 0
window.total = 0
window.show()
app.exec_()