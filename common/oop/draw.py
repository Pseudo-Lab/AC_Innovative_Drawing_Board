from common.algorithm.drawing_shapes import *
from PySide6 import QtWidgets, QtCore, QtGui


class Draw:

    q_graphic: QtWidgets.QGraphicsPixmapItem
    canvas: QtGui.QPixmap
    lastPoint: QtCore.QPoint
    pointlist: list             # 그리기 좌표를 저장합니다.

    def __init__(self):
        super(Draw, self).__init__()

    # 좌표 지우기
    def removePrevPoints(self):

        # 지우개 생성
        rubber = QtGui.QPen()
        a: int = 20
        rubber.setWidth(a)
        rubber.setColor(QtGui.Qt.white)

        # 지우개 장착
        painter = QtGui.QPainter(self.canvas)
        painter.setPen(rubber)

        for rpoint in self.pointlist:
            painter.drawPoint(QtCore.QPoint(rpoint[0][0], rpoint[0][1]))
        painter.end()
        self.q_graphic.setPixmap(self.canvas)

    def ellipse(self):
        self.removePrevPoints()
        ret = np.array(self.pointlist)

        # 페인트 생성
        painter = QtGui.QPainter(self.canvas)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

        # 타원 그리기
        listofpoints = draw_ellipse(ret)
        firstPoint = QtCore.QPoint()
        for count, item in enumerate(listofpoints):  # , start=1):
            if count == 0:
                self.lastPoint = QtCore.QPoint(item[0], item[1])
                firstPoint = QtCore.QPoint(item[0], item[1])
            else:
                painter.drawLine(self.lastPoint, QtCore.QPoint(item[0], item[1]))
                self.lastPoint = QtCore.QPoint(item[0], item[1])
        painter.drawLine(self.lastPoint, firstPoint)

        painter.end()

        self.q_graphic.setPixmap(self.canvas)
        self.pointlist.clear()

    def circle(self):
        self.removePrevPoints()
        ret = np.array(self.pointlist)

        # 캔버스 가져오기
        canvas = self.q_graphic.pixmap()

        # 페인트 생성
        painter = QtGui.QPainter(canvas)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

        # 원 그리기
        listofpoints = draw_circle(ret)
        firstPoint = QtCore.QPoint()
        for count, item in enumerate(listofpoints):  # , start=1):
            if count == 0:
                self.lastPoint = QtCore.QPoint(item[0], item[1])
                firstPoint = QtCore.QPoint(item[0], item[1])
            else:
                painter.drawLine(self.lastPoint, QtCore.QPoint(item[0], item[1]))
                self.lastPoint = QtCore.QPoint(item[0], item[1])
        painter.drawLine(self.lastPoint, firstPoint)

        painter.end()

        self.q_graphic.setPixmap(canvas)
        self.pointlist.clear()

    def rotated_rect(self):
        self.removePrevPoints()
        ret = np.array(self.pointlist)

        # 캔버스 가져오기
        canvas = self.q_graphic.pixmap()

        # 페인트 생성
        painter = QtGui.QPainter(canvas)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

        # minRect 그리기
        boxx = draw_minRect(ret)

        # draw minRect
        painter.drawLine(QtCore.QPoint(boxx[0][0], boxx[0][1]), QtCore.QPoint(boxx[1][0], boxx[1][1]))
        painter.drawLine(QtCore.QPoint(boxx[1][0], boxx[1][1]), QtCore.QPoint(boxx[2][0], boxx[2][1]))
        painter.drawLine(QtCore.QPoint(boxx[2][0], boxx[2][1]), QtCore.QPoint(boxx[3][0], boxx[3][1]))
        painter.drawLine(QtCore.QPoint(boxx[3][0], boxx[3][1]), QtCore.QPoint(boxx[0][0], boxx[0][1]))
        painter.end()

        self.q_graphic.setPixmap(canvas)
        self.pointlist.clear()

    def rect(self):
        self.removePrevPoints()
        ret = np.array(self.pointlist)

        # 캔버스 가져오기
        canvas = self.q_graphic.pixmap()

        # 페인트 생성
        painter = QtGui.QPainter(canvas)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

        # boundingRect 그리기
        brect = draw_boundingRect(ret)

        # draw boundingRect
        painter.drawLine(QtCore.QPoint(brect[0], brect[1]), QtCore.QPoint(brect[0] + brect[2], brect[1]))
        painter.drawLine(QtCore.QPoint(brect[0] + brect[2], brect[1]),
                         QtCore.QPoint(brect[0] + brect[2], brect[1] + brect[3]))
        painter.drawLine(QtCore.QPoint(brect[0] + brect[2], brect[1] + brect[3]),
                         QtCore.QPoint(brect[0], brect[1] + brect[3]))
        painter.drawLine(QtCore.QPoint(brect[0], brect[1] + brect[3]), QtCore.QPoint(brect[0], brect[1]))

        painter.end()

        self.q_graphic.setPixmap(canvas)
        self.pointlist.clear()

    def pen(self, e):

        # 페인트 생성
        painter = QtGui.QPainter(self.canvas)

        # 페인트 그리기
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
        painter.drawLine(self.lastPoint, e.pos())
        painter.end()
        self.lastPoint = e.pos()
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