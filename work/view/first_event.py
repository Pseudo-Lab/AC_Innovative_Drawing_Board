from PySide6 import QtCore, QtGui
from common.oop.draw import Draw
from common.oop.shapes import Shapes
from work.view.first import First


class FirstEvent(First):
    """
        first 의
        event 클레스 입니다.
        Window 화면의 first view 의 mouse 이벤트가 일어나면 그리기를 합니다.
    """

    guide: Draw                 # 그리기 객체 입니다.
    shapes: Shapes              # 도형 객체 입니다.
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
        self.draw.canvas = self.canvas_draw
        self.draw.q_graphic = self.draw_graphic
        self.draw.lastPoint = self.lastPoint
        self.draw.pointlist = self.pointlist

        # 가이드 객체를 생성 합니다.
        self.guide = Draw()
        self.guide.canvas = self.canvas_guide
        self.guide.q_graphic = self.guide_graphic
        self.guide.lastPoint = self.lastPoint
        self.guide.pointlist = self.pointlist

        # 도형 객체를 생성 합니다.
        self.shapes = Shapes()
        self.shapes.canvas = self.canvas_shapes
        self.shapes.q_graphic = self.shapes_graphic
        self.shapes.lastPoint = self.lastPoint
        self.shapes.pointlist = self.pointlist

    # 사용자 마우스 이벤트 처리
    def mousePressEvent(self, e):
        print('FirstEvent: mousePressEvent')

        # 마우스 좌표에 스크롤 좌표 적용 위치 생성
        position = QtCore.QPoint(e.x() + self.scroll_x, e.y() + self.scroll_y)

        if e.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.lastPoint = position
            self.draw.lastPoint = position
            self.guide.lastPoint = position
            self.shapes.lastPoint = position

    def mouseReleaseEvent(self, e):
        print('FirstEvent: mouseReleaseEvent')

        self.drawing = False

        if self.draw_state is 'ellipse':
            self.shapes.ellipse()

        if self.draw_state is 'circle':
            self.shapes.circle()

        if self.draw_state is 'rotated_rect':
            self.shapes.rotated_rect()

        if self.draw_state is 'rect':
            self.shapes.rect()

        # 가이드 씬을 숨깁니다.
        self.guide_graphic.hide()

    def mouseMoveEvent(self, e):
        print('FirstEvent: mouseMoveEvent')

        # 가이드 씬을 보여 줍니다.
        self.guide_graphic.show()

        # 마우스 좌표에 스크롤 좌표 적용 위치 생성
        position = QtCore.QPoint(e.x() + self.scroll_x, e.y() + self.scroll_y)

        # 펜 그리기
        if self.draw_state is 'pen' and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            print('draw pen')
            self.draw.pen(position)

        # 지우개
        if self.draw_state is 'rubber':
            self.draw.rubber(position)
            self.guide.rubber(position)
            self.shapes.rubber(position)

        if (self.draw_state in ['ellipse', 'circle', 'rect', 'rotated_rect']) \
                and e.buttons() \
                and QtCore.Qt.LeftButton \
                and self.drawing:
            print('FirstEvent: mouseMoveEvent -> end')

            # 페인트 생성
            painter = QtGui.QPainter(self.canvas_guide)

            # 페인트 그리기
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
            painter.drawLine(self.guide.lastPoint, position)
            painter.end()

            # 가이드 좌표 저장
            self.guide.lastPoint = position
            self.guide.pointlist.append([[e.x() + self.scroll_x, e.y() + self.scroll_y]])

            # 가이드와 도형 픽스맵 업데이트
            self.guide_graphic.setPixmap(self.canvas_guide)
            self.shapes_graphic.setPixmap(self.canvas_shapes)
