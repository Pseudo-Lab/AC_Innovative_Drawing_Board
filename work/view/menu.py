from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenuBar


class Menu(QMenuBar):

    call_exit = None     # 콜백 메소드: 종료 호출
    exitAction: QAction  # 종료 버튼

    def __init__(self, target_obj):
        super().__init__()

        # 종료 액션 생성
        self.exitAction = QAction(QIcon(None), 'Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.file_button_click)

        # 메뉴에 액션 등록
        file_menu = self.addMenu('&File')
        file_menu.addAction(self.exitAction)

    # # mark - Event Method
    def file_button_click(self):
        print("Menu: file_button_click -> exit")
        call = self.call_exit
        call()
