from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenuBar


class Menu(QMenuBar):

    call_exit = None        # 콜백 메소드: 종료 호출
    call_image_load = None  # 콜백 메소드: 이미지 로드
    call_style_load = None  # 콜백 메소드: 스타일 로드
    exitAction: QAction     # 종료 버튼

    def __init__(self):
        super().__init__()
        print('Menu: init')

        # 이미지 불러오기 액션 생성
        self.loadAction = QAction(QIcon(None), 'Image Load', self)
        self.loadAction.triggered.connect(self.image_file_load)

        # 스타일 불러오기 액션 생성
        self.styleAction = QAction(QIcon(None), 'Style Load', self)
        self.styleAction.triggered.connect(self.style_file_load)

        # 종료 액션 생성
        self.exitAction = QAction(QIcon(None), 'Exit', self)
        self.exitAction.triggered.connect(self.file_app_close)
        self.exitAction.setShortcut('Ctrl+Q')

        # 메뉴에 액션 등록
        file_menu = self.addMenu('&File')
        file_menu.addAction(self.loadAction)
        file_menu.addAction(self.styleAction)
        file_menu.addAction(self.exitAction)

    # mark - Event Method
    def file_app_close(self):
        print("Menu: file_app_close")
        call = self.call_exit
        call()

    def image_file_load(self):
        print("Menu: image_file_load")
        call = self.call_image_load
        call()

    def style_file_load(self):
        print("Menu: style_file_load")
        call = self.call_style_load
        call()