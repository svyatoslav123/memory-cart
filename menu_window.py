from PyQt5.QtWidgets import *

from main import h1


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Введіть правильну")
    quest_edit = QLineEdit()
    right_ans_lbl = QLineEdit()

    main_line =  QVBoxLayout()
    h1.QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)
def add_quest_func():
    a = {
        "Запитання" : quest_edit.text(),
        "Правильна відповідь": "",
        "Неправилна 1": "",
        "Неправилна 2": "",
        "Неправилна 3": "",


    }
    dates
    window.exec()