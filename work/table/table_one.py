from PySide6.QtWidgets import *


class TableOne:
    top_widget = None
    top_layout = None
    group_layout = None

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
            push_button = QPushButton()
            push_button.setText(index)
            push_button.clicked.connect(self.click_event)
            push_button.setFixedSize(170, 80)

            # 스크롤의 가장 위에 보여질 그룹박스
            self.top_layout.addWidget(push_button)
            self.top_widget.setLayout(self.top_layout)

            i = i + 1

    # mark - Event call back Method
    def click_event(self):
        print('TableOne: click_event')
