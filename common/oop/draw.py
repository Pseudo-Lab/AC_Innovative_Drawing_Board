
from PySide6 import QtWidgets, QtCore, QtGui


class Draw:

    q_graphic: QtWidgets.QGraphicsPixmapItem
    canvas: QtGui.QPixmap
    lastPoint: QtCore.QPoint
    pointlist: list             # 그리기 좌표를 저장합니다.

    def __init__(self):
        super(Draw, self).__init__()

    def pen(self, e):

        # 페인트 생성
        painter = QtGui.QPainter(self.canvas)

        # 페인트 그리기
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
        painter.drawLine(self.lastPoint, e)
        painter.end()
        self.lastPoint = e

        # 캔버스 업데이트
        self.q_graphic.setPixmap(self.canvas)

    def rubber(self, e):
        # 지우개 생성
        rubber = QtGui.QPen()
        a: int = 10
        rubber.setWidth(a)
        rubber.setColor(QtGui.Qt.white)

        # 지우개 장착
        painter = QtGui.QPainter(self.canvas)
        painter.setPen(rubber)
        painter.drawPoint(e.x(), e.y())
        painter.end()

        # 캔버스 업데이트
        self.q_graphic.setPixmap(self.canvas)