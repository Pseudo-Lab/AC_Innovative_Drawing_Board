from PySide6 import QtCore, QtGui
from common.oop.draw import Draw
from work.view.first import First

'''
    first 의 
    event 클레스 입니다. 
    Window 화면의 first view 의 mouse 이벤트가 일어나면 그리기를 합니다.
'''


class FirstEvent(First):

    draw: Draw                  # 그리기 객체 입니다.
    lastPoint: QtCore.QPoint    # 그리기 마지막 포인트
    pointlist: list             # 그리기 좌표를 저장 합니다.

    def __init__(self, parent=None):
        super(FirstEvent, self).__init__(parent)
        print('FirstEvent: init')

        # 생성
        self.lastPoint = QtCore.QPoint()
        self.pointlist = []

        # 그리기 객체를 생성 합니다.
        self.draw = Draw()
        self.draw.canvas = self.canvas
        self.draw.q_graphic = self.q_graphic
        self.draw.lastPoint = self.lastPoint
        self.draw.pointlist = self.pointlist

    # 사용자 마우스 이벤트 처리
    def mousePressEvent(self, e):
        print('FirstEvent: mousePressEvent')

        position = QtCore.QPoint(e.x() + self.scroll_x, e.y() + self.scroll_y)

        if e.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.draw.lastPoint = position

    def mouseReleaseEvent(self, e):
        print('FirstEvent: mouseReleaseEvent')

        self.drawing = False

        if self.draw_state is 'ellipse':
            self.draw.ellipse()

        if self.draw_state is 'circle':
            self.draw.circle()

        if self.draw_state is 'rotated_rect':
            self.draw.rotated_rect()

        if self.draw_state is 'rect':
            self.draw.rect()

    def mouseMoveEvent(self, e):
        print('FirstEvent: mouseMoveEvent')

        position = QtCore.QPoint(e.x() + self.scroll_x, e.y() + self.scroll_y)

        # 펜 그리기
        if self.draw_state is 'pen' and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            self.draw.pen(position)

        # 지우개
        if self.draw_state is 'rubber':
            self.draw.rubber(position)

        if (self.draw_state in ['ellipse', 'circle', 'rect',
                                'rotated_rect']) and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            print('FirstEvent: mouseMoveEvent -> end')

            # 페인트 생성
            painter = QtGui.QPainter(self.draw.canvas)

            # 페인트 그리기
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
            painter.drawLine(self.draw.lastPoint, position)
            painter.end()
            self.draw.lastPoint = position
            self.draw.pointlist.append([[e.x() + self.scroll_x, e.y() + self.scroll_y]])
            # 캔버스 업데이트
            self.q_graphic.setPixmap(self.draw.canvas)
