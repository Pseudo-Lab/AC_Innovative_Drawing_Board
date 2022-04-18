from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *

from work.view.first_event_extend import FirstEventExtend
from work.table.table_one import TableOne


class WindowControl(QWidget):
    """ VIEW """
    first_view = None       # 화면에 보여지는 image VIEW 입니다.
    img_scroll = None       # 스크롤 이미지 테이블
    table_one = None        # 첫번째 테이블
    current_image: QPixmap  # 사용자 불러오기 현재 이미지

    def __init__(self):
        super().__init__()
        print('WindowControl: init')

        # roi 리스트 생성
        self.roi_list = []

        # View 생성
        self.first_view = FirstEventExtend()
        self.first_view.setup()

        # 스크롤과 테이블 생성
        self.table_one = TableOne()
        self.img_scroll = QScrollArea()

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.table_one.create(data)
        self.img_scroll.setWidget(self.table_one.top_widget)

        # ui view 실행
        self.view_setup()

    def view_setup(self):
        print('WindowControl: view_setup')

        # 레이아웃 생성
        form_box = QVBoxLayout()

        # 하위 레이아웃 생성
        top = QVBoxLayout()
        center = QHBoxLayout()
        _view = QHBoxLayout()
        _right = QHBoxLayout()

        # 창 늘여도 좌측 상단 고정
        center.setAlignment(QtCore.Qt.AlignLeft)
        center.addLayout(_view)
        center.addLayout(_right)

        # 위젯 장착
        _view.addWidget(self.first_view, alignment=QtCore.Qt.AlignRight)
        _view.addWidget(self.img_scroll, alignment=QtCore.Qt.AlignLeft)

        # 폼박스에 레이아웃 넣기
        form_box.addLayout(top)
        form_box.addLayout(center)

        # 레이아웃에 폼박스 등록
        self.setLayout(form_box)

    def view_image_update(self, path):
        print('WindowControl: view_image_update')
        self.first_view.canvas.load(path)
        self.first_view.repaint()
