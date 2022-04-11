from PySide6 import QtWidgets, QtGui, QtCore
from config import setting

import ctypes


# 모니터 화면 사이즈
def get_size():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    f'{screen_width}, {screen_height}'
    return screen_width, screen_height


class First(QtWidgets.QGraphicsView):

    screen_rect = None      # 화면에 보여지는 이미지 사각형 크기
    canvas: QtGui.QPixmap   # 픽스맵
    draw_state = 'pen'      # 그리기 상태
    drawing = True          # 그리기 액션 판정

    # 기본 뷰 생성
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.q_graphic)
        self.setScene(self.scene)

        # 캔버스 세팅
        w, h = get_size()
        self.canvas = QtGui.QPixmap(w, h)
        self.canvas.fill(QtGui.Qt.white)
        self.q_graphic.setPixmap(self.canvas)

    # 뷰 세팅
    def setup(self):
        w, h = get_size()
        self.screen_rect: QtCore.QRectF = QtCore.QRectF(0.0, 0.0,
                                                        w,
                                                        h)

        self.setSceneRect(QtCore.QRectF(self.screen_rect))







