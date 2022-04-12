import sys
import main
from PySide6.QtWidgets import QApplication
from work.window import Window


def description():
    """
    프로그램의 시작 점 입니다.

    윈도우 클레스를 생성하고 실행 합니다.

    Classes:
        Window: 프로그램에 필요한 위젯을 생성하고 사용자 액션을 관리 합니다.
    """


if __name__ == '__main__':

    help(main)

    app = QApplication(sys.argv)
    window: Window = Window()
    sys.exit(app.exec())
