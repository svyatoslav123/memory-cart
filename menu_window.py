from PyQt5.QtWidgets import *

import dates



def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Введіть правильну")
    quest_edit = QLineEdit()
    right_ans_lbl = QLineEdit()
    add_quest_btn = QPushButton()






    main_line =  QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)
    def add_quest_func():
        a = {
            "Запитання" : quest_edit.text(),
            "Правильна відповідь": "",
            "Неправильна 1": "",
            "Неправильна 2": "",
            "Неправильна 3": "",


        }
        dates.questions.append(a)
    main_line.addWidget(add_quest_btn)
    add_quest_btn.clicked.connect(add_quest_func)
    window.setLayout(main_line)
    window.exec()