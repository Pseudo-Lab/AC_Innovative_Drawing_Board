from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, QIcon

from .window_control import WindowControl
from work.view.menu import Menu


class Window(QMainWindow):

    menu: Menu

    def __init__(self):
        super(Window, self).__init__()

        # 윈도우 메뉴 생성
        self.menu = Menu(self)

        # 윈도우 툴바 생성
        self.toolbar = self.addToolBar('Exit')

        # ui 실행
        self.ui_setup()

    def ui_setup(self):

        # Menu 종료 버튼
        exit_button = QAction(QIcon(None), "&Exit", self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(self.close)

        # Menu 버튼 등록
        self.toolbar.addAction(self.menu.file_button)
        self.toolbar.addAction(self.menu.help_button)
        self.toolbar.addAction(exit_button)

        # 윈도우 뷰 컨트롤 등록
        window_control = WindowControl()
        self.setCentralWidget(window_control)

        # 윈도우 화면 시작
        self.show()
