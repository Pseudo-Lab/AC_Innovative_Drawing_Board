import sys
from PySide6.QtWidgets import QApplication

from work.windows import Window


if __name__ == '__main__':
    print('main')

    app = QApplication(sys.argv)
    window: Window = Window()
    sys.exit(app.exec())
