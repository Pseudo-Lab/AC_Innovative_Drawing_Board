
from common.algorithm.drawing_shapes import *
from common.oop.draw import Draw
from PySide6 import QtCore, QtGui


class Shapes(Draw):

    def __init__(self):
        super(Shapes, self).__init__()


    def ellipse(self):
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
        ret = np.array(self.pointlist)

        # 페인트 생성
        painter = QtGui.QPainter(self.canvas)
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

        self.q_graphic.setPixmap(self.canvas)
        self.pointlist.clear()

    def rotated_rect(self):
        ret = np.array(self.pointlist)

        # 페인트 생성
        painter = QtGui.QPainter(self.canvas)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

        # minRect 그리기
        boxx = draw_minRect(ret)

        # draw minRect
        painter.drawLine(QtCore.QPoint(boxx[0][0], boxx[0][1]), QtCore.QPoint(boxx[1][0], boxx[1][1]))
        painter.drawLine(QtCore.QPoint(boxx[1][0], boxx[1][1]), QtCore.QPoint(boxx[2][0], boxx[2][1]))
        painter.drawLine(QtCore.QPoint(boxx[2][0], boxx[2][1]), QtCore.QPoint(boxx[3][0], boxx[3][1]))
        painter.drawLine(QtCore.QPoint(boxx[3][0], boxx[3][1]), QtCore.QPoint(boxx[0][0], boxx[0][1]))

        painter.end()

        self.q_graphic.setPixmap(self.canvas)
        self.pointlist.clear()

    def rect(self):
        ret = np.array(self.pointlist)

        # 페인트 생성
        painter = QtGui.QPainter(self.canvas)
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

        self.q_graphic.setPixmap(self.canvas)
        self.pointlist.clear()