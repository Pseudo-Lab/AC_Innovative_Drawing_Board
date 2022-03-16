from PySide6 import QtWidgets, QtCore


class First(QtWidgets.QGraphicsView):
    screen_rect = None  # 화면에 보여지는 이미지 사각형 크기

    # QT 예제 기본 VIEW 구조
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.q_graphic)
        self.setScene(self.scene)

    def setup(self):
        self.screen_rect: QtCore.QRectF = QtCore.QRectF(0.0, 0.0, 600, 500)
        self.setSceneRect(QtCore.QRectF(self.screen_rect))



