from PySide6.QtWidgets import *
from PySide6 import QtCore


class TableButton(QPushButton):
    def __init__(self, btn_id, parent=None):
        super().__init__(parent)
        self.btn_id = btn_id

    def get_button_id(self):
        return self.btn_id


class TableOne:
    top_widget = None
    top_layout = None
    group_layout = None
    buttonGroup = QButtonGroup()

    def __init__(self):
        super().__init__()

    def create(self, data_list):
        self.top_widget = QWidget()
        self.top_layout = QVBoxLayout()

        i = 0
        for _ in data_list:
            # 버튼에 표시 되는 숫자 1부터
            index = f'{i+1}'

            # 그룹박스 레이아웃에 들어가는 버튼
            push_button = TableButton(index)
            push_button.setText(index)
            push_button.clicked.connect(lambda stat=False, obj=push_button: self.click_event(obj))
            push_button.setFixedSize(170, 50)
            self.buttonGroup.addButton(push_button, i)

            # 스크롤의 가장 위에 보여질 그룹박스
            self.top_layout.addWidget(push_button, alignment=QtCore.Qt.AlignLeft)
            self.top_widget.setLayout(self.top_layout)

            i = i + 1

    # mark - Event call back Method
    @ classmethod
    def click_event(cls, obj):
        btn: QPushButton = obj
        print('TableOne: click_event', btn.get_button_id())

