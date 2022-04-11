from PySide6 import QtCore, QtGui

from work.view.first_event import FirstEvent

'''
    first_event 의 
    확장(extends) 클레스 입니다. 
    Window 화면의 first view 의 사용자 이벤트를 처리 합니다.
'''


class FirstEventExtend (FirstEvent):

    def __init__(self, parent=None):
        super(FirstEventExtend, self).__init__(parent)

    # 사용자 이벤트 처리
    def userEvent(self, event):

        user_event = event

        # 화면 리셋
        if user_event is 'reset':
            print('FirstEventExtend: userEvent -> reset')

            # 화면 채우기
            self.canvas.fill(QtGui.Qt.white)

            # 캔버스 업데이트
            self.q_graphic.setPixmap(self.canvas)

