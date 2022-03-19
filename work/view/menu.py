from PySide6.QtGui import QAction, QIcon


class Menu:

    exit_button: QAction    # 종료 버튼
    file_button: QAction    # 파일 버튼
    help_button: QAction    # 헬프 버튼

    def __init__(self, target_obj):
        super().__init__()

        # 파일 버튼
        self.file_button = QAction(QIcon(None), "&File", target_obj)
        self.file_button.triggered.connect(self.file_button_click)
        self.file_button.setCheckable(True)

        # 헬프 버튼
        self.help_button = QAction(QIcon(None), "&Help", target_obj)
        self.help_button.triggered.connect(self.help_button_click)
        self.help_button.setCheckable(True)

    # mark - Event Method
    def file_button_click(self, s):
        print("file_button_click", s)

    # mark - Event Method
    def help_button_click(self, s):
        print("help_button_click", s)