import time


class Sketch:

    """
    sketch 그리기 속성 입니다.
    object model class 입니다.
    """

    pointlist: list
    draw_type: str
    draw_size: int
    draw_fill: bool
    draw_color: None

    time_start: time
    time_end: time

    def __init__(self):
        print('Sketch: init')
        print(self.__doc__)
