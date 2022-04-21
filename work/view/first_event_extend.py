from PySide6 import QtCore, QtGui

from work.view.first_event import FirstEvent


class FirstEventExtend (FirstEvent):
    """
        first_event 의
        확장(extends) 클레스 입니다.
        Window 화면의 first view 의 사용자 이벤트를 처리 합니다.
    """

    def __init__(self, parent=None):
        super(FirstEventExtend, self).__init__(parent)
        print(self.__doc__)

    # 사용자 이벤트 처리
    def userEvent(self, event):

        user_event = event

        # 화면 리셋
        if user_event is 'reset':
            print('FirstEventExtend: userEvent -> reset')

            # 투명 컬러를 만듭니다.
            color = QtGui.QColor(0)
            color.setAlpha(0)

            # 화면 채우기
            self.canvas.fill(QtGui.Qt.white)
            self.canvas_draw.fill(color)
            self.canvas_guide.fill(color)
            self.canvas_shapes.fill(color)

            # 캔버스 업데이트
            self.q_graphic.setPixmap(self.canvas)
            self.draw_graphic.setPixmap(self.canvas_draw)
            self.guide_graphic.setPixmap(self.canvas_guide)
            self.shapes_graphic.setPixmap(self.canvas_shapes)

