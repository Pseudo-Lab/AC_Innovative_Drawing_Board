from PySide6.QtWidgets import *

from .window_control import WindowControl
from work.view.menu import Menu
from work.view.tool import Tool


class Window(QMainWindow):

    window_control: WindowControl   # 윈도우 뷰 컨트롤러
    menu: Menu                      # 최상단 메뉴 입니다.
    tool: Tool                      # 최상단 툴바 입니다.

    def __init__(self):
        super(Window, self).__init__()

        # 윈도우 뷰 컨트롤러 생성
        self.window_control = WindowControl()

        # 윈도우 메뉴 생성
        self.menu = Menu()

        # 윈도우 툴바 생성
        self.tool = Tool()

        # 콜백 메소드 등록
        self.call_register()

        # ui 실행
        self.ui_setup()

    def ui_setup(self):
        # 메뉴 등록
        self.setMenuWidget(self.menu)

        # 툴바 등록
        self.addToolBar(self.tool)

        # 윈도우 뷰 컨트롤 등록
        self.setCentralWidget(self.window_control)

        # 윈도우 화면 시작
        self.show()

    def call_register(self):
        # 메뉴: 종료 버튼
        self.menu.call_exit = self.menu_app_exit

        # 그리기 상태
        self.tool.call_pen = self.draw_state
        self.tool.call_rubber = self.draw_state
        self.tool.call_cut = self.draw_state
        self.tool.call_paint = self.draw_state

        # 사용자 이벤트
        self.tool.call_reset = self.user_event

    # mark - call back method
    def menu_app_exit(self):
        print('Window: menu_app_exit')
        self.close()

    # mark - call back method
    def draw_state(self, state):
        print('Window: draw_state')
        self.window_control.first_view.draw_state = state

    # mark - user event method
    def user_event(self, event):
        print('Window: user_event')
        self.window_control.first_view.userEvent(event)