from PySide6 import QtWidgets, QtCore, QtGui

from config import setting
import numpy as np
import cv2
import math



class First(QtWidgets.QGraphicsView):

    screen_rect = None  # 화면에 보여지는 이미지 사각형 크기
    pointlist = []
    draw_state = 'pen'  # 그리기 상태
    drawing = True      # 그리기 액션 판정

    # 기본 뷰 생성
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.q_graphic)
        self.setScene(self.scene)
        self.lastPoint = QtCore.QPoint()

        # 캔버스 세팅
        canvas = QtGui.QPixmap(700, 550)
        canvas.fill(QtGui.Qt.white)
        self.q_graphic.setPixmap(canvas)

    def draw_ellipse(self, ecenter, esize, erotation):
        cx, cy = ecenter[0], ecenter[1]
        rx, ry = esize[0], esize[1]
        # 캔버스 가져오기
        canvas = self.q_graphic.pixmap()

        # 페인트 생성
        painter = QtGui.QPainter(canvas)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))
        for i in np.arange(0, 2 * math.pi, 0.1):
            if i > 0:
                x1 = cx - (ry * 0.5 * math.sin(i - 1)) * math.sin(erotation) + (rx * 0.5 * math.cos(i - 1)) * math.cos(
                    erotation)
                y1 = cy + (rx * 0.5 * math.cos(i - 1)) * math.sin(erotation) + (ry * 0.5 * math.sin(i - 1)) * math.cos(
                    erotation)
                x2 = cx - (ry * 0.5 * math.sin(i)) * math.sin(erotation) + (rx * 0.5 * math.cos(i)) * math.cos(
                    erotation)
                y2 = cy + (rx * 0.5 * math.cos(i)) * math.sin(erotation) + (ry * 0.5 * math.sin(i)) * math.cos(
                    erotation)
                first_point = QtCore.QPoint(x1, y1)
                second_point = QtCore.QPoint(x2, y2)
                painter.drawLine(first_point, second_point)
        painter.end()
        self.q_graphic.setPixmap(canvas)

    # 뷰 세팅
    def setup(self):
        self.screen_rect: QtCore.QRectF = QtCore.QRectF(0.0, 0.0,
                                                        setting.VIEW_DEFAULT_WIDTH,
                                                        setting.VIEW_DEFAULT_HEIGHT)

        self.setSceneRect(QtCore.QRectF(self.screen_rect))

    # 사용자 마우스 이벤트 처리
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.lastPoint = e.pos()


    def mouseReleaseEvent(self, e):
        self.drawing = False

        if self.draw_state is 'ellipse':
            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 지우개 생성
            rubber = QtGui.QPen()
            a: int = 10
            rubber.setWidth(a)
            rubber.setColor(QtGui.Qt.white)

            # 지우개 장착
            painter = QtGui.QPainter(canvas)
            painter.setPen(rubber)

            for rpoint in self.pointlist:
                painter.drawPoint(QtCore.QPoint(rpoint[0][0],rpoint[0][1]))
            painter.end()
            self.q_graphic.setPixmap(canvas)

            ret = np.array(self.pointlist)
            rrt = cv2.fitEllipse(ret)

            self.draw_ellipse(rrt[0],rrt[1],rrt[2])
            self.pointlist.clear()

    def mouseMoveEvent(self, e):
        
        # 펜 그리기
        if self.draw_state is 'pen' and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            print('mouseMoveEvent: pen')

            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)

            # 페인트 그리기
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
            painter.drawLine(self.lastPoint, e.pos())
            painter.end()
            self.lastPoint = e.pos()
            # 캔버스 업데이트
            self.q_graphic.setPixmap(canvas)

        # 지우개
        if self.draw_state is 'rubber':
            print('mouseMoveEvent: rubber')

            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 지우개 생성
            rubber = QtGui.QPen()
            a: int = 10
            rubber.setWidth(a)
            rubber.setColor(QtGui.Qt.white)

            # 지우개 장착
            painter = QtGui.QPainter(canvas)
            painter.setPen(rubber)
            painter.drawPoint(e.x(), e.y())
            painter.end()

            # 캔버스 업데이트
            self.q_graphic.setPixmap(canvas)

        if self.draw_state is 'ellipse' and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            print('mouseMoveEvent: pen')

            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)

            # 페인트 그리기
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
            painter.drawLine(self.lastPoint, e.pos())
            painter.end()
            self.lastPoint = e.pos()
            self.pointlist.append([[e.x(), e.y()]])
            # 캔버스 업데이트
            self.q_graphic.setPixmap(canvas)





