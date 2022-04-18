from PySide6.QtWidgets import *


class Reason(QVBoxLayout):

    def __init__(self, parent=None):
        super(Reason, self).__init__(parent)

        button_1 = QPushButton('Reason')
        imsi = 1
        button_1.clicked.connect(lambda stat=False, parameter=imsi: self.push_event(parameter))
        self.addWidget(button_1)

    def push_event(self, value):
        print('Reason: push_event ->', value)



