from PySide6 import QtWidgets, QtGui, QtCore
from common.util import monitor


class First(QtWidgets.QGraphicsView):

    canvas: QtGui.QPixmap           # 픽스맵
    canvas_guide: QtGui.QPixmap     # 피스맵 가이드
    draw_state = 'pen'              # 그리기 상태
    drawing = True                  # 그리기 액션 판정
    screen_rect = None              # 화면에 보여지는 이미지 사각형 크기
    scroll_x = None                 # 스크롤 바 x 값
    scroll_y = None                 # 스크롤 바 y 값

    # 기본 뷰 생성
    def __init__(self, parent=None):
        super(First, self).__init__(parent)

        # Scene 생성
        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()
        self.guide_graphic = QtWidgets.QGraphicsPixmapItem()

        # 씬에 픽스 맵을 추가합니다.
        self.scene.addItem(self.q_graphic)
        self.scene.addItem(self.guide_graphic)
        self.setScene(self.scene)

        # 투명 컬러를 만듭니다.
        color = QtGui.QColor(0)
        color.setAlpha(0)

        # 캔버스 세팅
        w, h = monitor.get_size()
        self.canvas = QtGui.QPixmap(w, h)
        self.canvas.fill(QtGui.Qt.white)
        self.q_graphic.setPixmap(self.canvas)

        # 투명 백그라운드를 가진 캔버스 가이드를 세팅 합니다.
        self.canvas_guide = QtGui.QPixmap(w, h)
        self.canvas_guide.fill(color)
        self.guide_graphic.setPixmap(self.canvas_guide)

        # 스크롤 바 바인딩
        x_bar = self.horizontalScrollBar()
        y_bar = self.verticalScrollBar()
        x_bar.valueChanged.connect(lambda value: self.scrolled_x(value))
        y_bar.valueChanged.connect(lambda value: self.scrolled_y(value))

        # 스트롤 바 초기화
        self.scroll_x = 0
        self.scroll_y = 0

    # 뷰 세팅
    def setup(self):
        w, h = monitor.get_size()
        self.screen_rect: QtCore.QRectF = QtCore.QRectF(0.0, 0.0, w, h)
        self.setSceneRect(QtCore.QRectF(self.screen_rect))

    # 뷰 스크롤 x 이동
    def scrolled_x(self, value):
        self.scroll_x = value

    # 뷰 스크롤 y 이동
    def scrolled_y(self, value):
        self.scroll_y = value




