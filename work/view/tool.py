from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import *


class Tool(QToolBar):

    input_label = None

    def __init__(self, parent=None):
        super(Tool, self).__init__(parent)
        print('Tool: init')

        # 도움 액션 생성
        self.helpAction = QAction(QIcon(None), 'help', self)
        self.helpAction.triggered.connect(self.help_button_click)

        # 액션 등록
        self.addAction(self.helpAction)

    def help_button_click(self):
        print('Tool: help_button_click')

