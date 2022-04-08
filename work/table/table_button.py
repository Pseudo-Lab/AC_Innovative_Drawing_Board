from PySide6.QtWidgets import *

class TableButton(QPushButton):
    def __init__(self, btn_id, parent=None):
        super().__init__(parent)
        self.btn_id = btn_id

    def get_button_id(self):
        return self.btn_id