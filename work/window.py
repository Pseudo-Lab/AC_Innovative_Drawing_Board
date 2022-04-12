from PySide6.QtWidgets import *

from .window_control import WindowControl
from work.view.menu import Menu
from work.view.tool import Tool
from config import setting


class Window(QMainWindow):

    window_control: WindowControl   # 윈도우 뷰 컨트롤러
    menu: Menu                      # 최상단 메뉴 입니다.
    tool: Tool                      # 최상단 툴바 입니다.

    def __init__(self):
        super(Window, self).__init__()
        print('Window: init')

        # 윈도우 메뉴 생성
        self.menu = Menu()

        # 윈도우 툴바 생성
        self.tool = Tool()

        # 윈도우 세팅
        self.setWindowTitle(setting.TITLE_WINDOW)
        self.setGeometry(0, 0, setting.WINDOW_SCREEN_WIDTH, setting.WINDOW_SCREEN_HEIGHT)

        # 윈도우 뷰 컨트롤러 생성
        self.window_control = WindowControl()

        # 콜백 메소드 등록
        self.call_register()

        # ui 실행
        self.ui_setup()

    def ui_setup(self):
        """
        Window: Register the widget show on the screen.
        """
        print(self.ui_setup.__doc__)

        # 메뉴 등록
        self.setMenuWidget(self.menu)

        # 툴바 등록
        self.addToolBar(self.tool)

        # 윈도우 뷰 컨트롤 등록
        self.setCentralWidget(self.window_control)

        # 윈도우 화면 시작
        self.show()

    def call_register(self):
        """
        Window: call_register
        """
        print(self.call_register.__doc__)

        # 메뉴: 종료 버튼
        self.menu.call_exit = self.menu_app_exit

        # 그리기 상태
        self.tool.call_pen = self.draw_state
        self.tool.call_rubber = self.draw_state
        self.tool.call_cut = self.draw_state
        self.tool.call_paint = self.draw_state
        self.tool.call_ellipse = self.draw_state
        self.tool.call_circle = self.draw_state
        self.tool.call_rect = self.draw_state
        self.tool.call_rotated_rect = self.draw_state

        # 사용자 이벤트
        self.tool.call_reset = self.user_event

    def menu_app_exit(self):
        """
        call back method
        """
        print(self.menu_app_exit.__doc__)
        self.close()

    # mark - call back method
    def draw_state(self, state):
        """
        call back method
        """
        print(self.draw_state.__doc__)
        self.window_control.first_view.draw_state = state

    # mark - user event method
    def user_event(self, event):
        """
        call back method
        """
        print(self.user_event.__doc__)
        self.window_control.first_view.userEvent(event)