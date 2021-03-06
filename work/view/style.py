from PySide6 import QtWidgets, QtGui, QtCore


class Style(QtWidgets.QGraphicsView):

    screen_rect = None      # 화면에 보여지는 이미지 사각형 크기

    # 기본 뷰 생성
    def __init__(self, parent=None):
        super(Style, self).__init__(parent)

        # Scene 생성
        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.q_graphic)
        self.setScene(self.scene)

        # 캔버스 세팅
        self.canvas = QtGui.QPixmap(255, 465)
        self.canvas.fill(QtGui.Qt.blue)
        self.q_graphic.setPixmap(self.canvas)

    # 뷰 세팅
    def setup(self):
        self.screen_rect: QtCore.QRectF = QtCore.QRectF(0.0, 0.0, 255, 465)
        self.setSceneRect(QtCore.QRectF(self.screen_rect))
