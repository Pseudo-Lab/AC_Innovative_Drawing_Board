from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, QIcon

from .window_control import WindowControl
from work.view.menu import Menu


class Window(QMainWindow):

    menu: Menu

    def __init__(self):
        super(Window, self).__init__()

        self.menu = Menu(self)
        self.toolbar = self.addToolBar('Exit')

        self.ui_setup()

    def ui_setup(self):

        exit_button = QAction(QIcon(None), "&Exit", self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(self.close)

        self.toolbar.addAction(self.menu.file_button)
        self.toolbar.addAction(self.menu.help_button)
        self.toolbar.addAction(exit_button)

        window_control = WindowControl()
        self.setCentralWidget(window_control)

        self.show()
