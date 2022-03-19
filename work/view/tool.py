from PySide6.QtWidgets import *


class Tool(QHBoxLayout):

    input_label = None

    def __init__(self, parent=None):
        super(Tool, self).__init__(parent)
        print('Tool: init')

        input_label = QLabel()
        input_label.setText('input..')

        self.addWidget(input_label)
