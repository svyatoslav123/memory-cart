from PyQt5.QtWidgets import *


import dates
def bublik():
    window = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Введіть правильну")
    wrong_ans_lbl1 = QLabel("Введіть неправильну1")
    wrong_ans_lbl2 = QLabel("Введіть неправильну2")
    wrong_ans_lbl3 = QLabel("Введіть неправильну3")

    quest_edit = QLineEdit()
    right_ans_input = QLineEdit()
    wrong_ans_input1 = QLineEdit()
    wrong_ans_input2 = QLineEdit()
    wrong_ans_input3 = QLineEdit()

    add_quest_btn = QPushButton()
    main_line: QVBoxLayout = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)
    h2 = QHBoxLayout()

    h2.addWidget(right_ans_lbl)
    h2.addWidget(right_ans_input)
    main_line.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(wrong_ans_lbl1)
    h3.addWidget(wrong_ans_input1)
    main_line.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(wrong_ans_lbl2)
    h4.addWidget(wrong_ans_input2)
    main_line.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(wrong_ans_lbl3)
    h5.addWidget(wrong_ans_input3)
    main_line.addLayout(h5)

    def add_quest_func():
        a = {
            "Запитання": quest_edit.text(),
            "Правильна відповідь": right_ans_input.text(),
            "Неправильна 1": wrong_ans_input1.text(),
            "Неправильна 2": wrong_ans_input2.text(),
            "Неправильна 3": wrong_ans_input3.text(),

        }
        dates.questions.append(a)

    main_line.addWidget(add_quest_btn)
    add_quest_btn.clicked.connect(add_quest_func)
    window.setLayout(main_line) main_line =  QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)
    h2 = QHBoxLayout()

    h2.addWidget(right_ans_lbl)
    h2.addWidget(right_ans_input)
    main_line.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(wrong_ans_lbl1)
    h3.addWidget(wrong_ans_input1)
    main_line.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(wrong_ans_lbl2)
    h4.addWidget(wrong_ans_input2)
    main_line.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(wrong_ans_lbl3)
    h5.addWidget(wrong_ans_input3)
    main_line.addLayout(h5)
    def add_quest_func():
        a = {
            "Запитання" : quest_edit.text(),
            "Правильна відповідь": right_ans_input.text(),
            "Неправильна 1": wrong_ans_input1.text(),
            "Неправильна 2": wrong_ans_input2.text(),
            "Неправильна 3": wrong_ans_input3.text(),


        }
        dates.questions.append(a)
    main_line.addWidget(add_quest_btn)
    add_quest_btn.clicked.connect(add_quest_func)
    window.setLayout(main_line)
    window.exec()