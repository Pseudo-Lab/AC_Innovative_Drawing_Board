from PySide6 import QtCore, QtGui
from common.oop.draw import Draw
from work.view.first import First

'''
    first 의 
    event 클레스 입니다. 
    Window 화면의 first view 의 mouse 이벤트가 일어나면 그리기를 합니다.
'''


class First_event(First):

    draw: Draw                  # 그리기 객체 입니다.
    lastPoint: QtCore.QPoint    # 그리기 마지막 포인트
    pointlist: list             # 그리기 좌표를 저장 합니다.

    def __init__(self, parent=None):
        super(First_event, self).__init__(parent)
        print('First_event: init')

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
        print('First_event: mousePressEvent')

        if e.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.draw.lastPoint = e.pos()

    def mouseReleaseEvent(self, e):
        print('First_event: mouseReleaseEvent')

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
        print('First_event: mouseMoveEvent')

        # 펜 그리기
        if self.draw_state is 'pen' and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            self.draw.pen(e)

        # 지우개
        if self.draw_state is 'rubber':
            self.draw.rubber(e)

        if (self.draw_state in ['ellipse', 'circle', 'rect',
                                'rotated_rect']) and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            print('First_event: mouseMoveEvent -> end')

            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)

            # 페인트 그리기
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
            painter.drawLine(self.draw.lastPoint, e.pos())
            painter.end()
            self.draw.lastPoint = e.pos()
            self.pointlist.append([[e.x(), e.y()]])
            # 캔버스 업데이트
            self.q_graphic.setPixmap(canvas)
