from PySide6.QtWidgets import *


def message(title, msg):
    print('Window: notice')
    buttonReply = QMessageBox.question(None, title, msg, QMessageBox.Yes)
    if buttonReply == QMessageBox.Yes:
        print('Yes clicked.')
