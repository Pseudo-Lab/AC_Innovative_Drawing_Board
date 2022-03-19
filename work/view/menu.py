from PySide6.QtGui import QAction, QIcon


class Menu:

    exit_button: QAction
    file_button: QAction
    help_button: QAction

    def __init__(self, target_obj):
        super().__init__()

        self.file_button = QAction(QIcon(None), "&File", target_obj)
        self.file_button.triggered.connect(self.file_button_click)
        self.file_button.setCheckable(True)

        self.help_button = QAction(QIcon(None), "&Help", target_obj)
        self.help_button.triggered.connect(self.help_button_click)
        self.help_button.setCheckable(True)

    def file_button_click(self, s):
        print("file_button_click", s)

    def help_button_click(self, s):
        print("help_button_click", s)