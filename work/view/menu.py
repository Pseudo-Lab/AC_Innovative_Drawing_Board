from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenuBar


class Menu(QMenuBar):

    call_exit = None        # 콜백 메소드: 종료 호출
    call_image_load = None  # 콜백 메소드: 이미지 로드
    exitAction: QAction     # 종료 버튼

    def __init__(self):
        super().__init__()
        print('Menu: init')

        # 이미지 불러오기 액션 생성
        self.loadAction = QAction(QIcon(None), 'Image Load', self)
        self.loadAction.triggered.connect(self.file_image_load)

        # 종료 액션 생성
        self.exitAction = QAction(QIcon(None), 'Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.file_app_close)

        # 메뉴에 액션 등록
        file_menu = self.addMenu('&File')
        file_menu.addAction(self.loadAction)
        file_menu.addAction(self.exitAction)

    # mark - Event Method
    def file_app_close(self):
        print("Menu: file_app_close")
        call = self.call_exit
        call()

    def file_image_load(self):
        print("Menu: file_image_load")
        call = self.call_image_load
        call()
