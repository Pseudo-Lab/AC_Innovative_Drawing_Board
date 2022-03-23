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
        self.menu.call_exit = self.menu_app_exit

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

    # mark - call back method
    def menu_app_exit(self):
        print('Window: menu_app_exit')
        self.close()
