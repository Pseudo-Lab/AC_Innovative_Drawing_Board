from PySide6 import QtWidgets, QtCore, QtGui

from config import setting
import numpy as np
import cv2
#import math
from common.algorithm.drawing_shapes import *


class First(QtWidgets.QGraphicsView):


    pointlist = []
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
        self.lastPoint = QtCore.QPoint()

        # 캔버스 세팅
        self.canvas = QtGui.QPixmap(700, 550)
        self.canvas.fill(QtGui.Qt.white)
        self.q_graphic.setPixmap(self.canvas)

    # 뷰 세팅
    def setup(self):
        self.screen_rect: QtCore.QRectF = QtCore.QRectF(0.0, 0.0,
                                                        setting.VIEW_DEFAULT_WIDTH,
                                                        setting.VIEW_DEFAULT_HEIGHT)

        self.setSceneRect(QtCore.QRectF(self.screen_rect))

    # 사용자 이벤트 처리
    def userEvent(self, event):

        user_event = event

        # 화면 리셋
        if user_event is 'reset':
            print('First: userEvent -> reset')

            # 화면 채우기
            self.canvas.fill(QtGui.Qt.white)

            # 캔버스 업데이트
            self.q_graphic.setPixmap(self.canvas)

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


            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

            # 타원 그리기
            listofpoints = draw_ellipse(ret)
            firstPoint =  QtCore.QPoint()
            for count, item in enumerate(listofpoints):#, start=1):
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

        if self.draw_state is 'circle':
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


            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

            # 원 그리기
            listofpoints = draw_circle(ret)
            firstPoint =  QtCore.QPoint()
            for count, item in enumerate(listofpoints):#, start=1):
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

        if self.draw_state is 'minRect':
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


            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

            # minRect 그리기
            boxx = draw_minRect(ret)

            #draw minRect
            painter.drawLine( QtCore.QPoint(boxx[0][0], boxx[0][1]),  QtCore.QPoint(boxx[1][0], boxx[1][1]))
            painter.drawLine( QtCore.QPoint(boxx[1][0], boxx[1][1]),  QtCore.QPoint(boxx[2][0], boxx[2][1]))
            painter.drawLine( QtCore.QPoint(boxx[2][0], boxx[2][1]),  QtCore.QPoint(boxx[3][0], boxx[3][1]))
            painter.drawLine( QtCore.QPoint(boxx[3][0], boxx[3][1]),  QtCore.QPoint(boxx[0][0], boxx[0][1]))
            painter.end()

            self.q_graphic.setPixmap(canvas)
            self.pointlist.clear()

        if self.draw_state is 'boundingRect':
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


            # 캔버스 가져오기
            canvas = self.q_graphic.pixmap()

            # 페인트 생성
            painter = QtGui.QPainter(canvas)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))

            # boundingRect 그리기
            brect = draw_boundingRect(ret)

            #draw boundingRect
            painter.drawLine(QtCore.QPoint(brect[0], brect[1]), QtCore.QPoint(brect[0] + brect[2], brect[1]))
            painter.drawLine(QtCore.QPoint(brect[0] + brect[2], brect[1]), QtCore.QPoint(brect[0] + brect[2], brect[1] + brect[3]))
            painter.drawLine(QtCore.QPoint(brect[0] + brect[2], brect[1] + brect[3]),QtCore.QPoint(brect[0], brect[1] + brect[3]))
            painter.drawLine(QtCore.QPoint(brect[0], brect[1] + brect[3]), QtCore.QPoint(brect[0], brect[1]))

            painter.end()

            self.q_graphic.setPixmap(canvas)
            self.pointlist.clear()

    def mouseMoveEvent(self, e):
        
        # 펜 그리기
        if self.draw_state is 'pen' and e.buttons() and QtCore.Qt.LeftButton and self.drawing:
            print('First: mouseMoveEvent: pen')

            # 페인트 생성
            painter = QtGui.QPainter(self.canvas)

            # 페인트 그리기
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))
            painter.drawLine(self.lastPoint, e.pos())
            painter.end()
            self.lastPoint = e.pos()
            # 캔버스 업데이트
            self.q_graphic.setPixmap(self.canvas)

        # 지우개
        if self.draw_state is 'rubber':
            print('First: mouseMoveEvent: rubber')

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





