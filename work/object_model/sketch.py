import time


class Sketch:

    """
    sketch 그리기 속성 입니다.

    object model class 입니다.

    Attributes:
        point list: 그리기 좌표를 저장 합니다.
        draw_type: 그리기 종류, 펜, 사각형, 타원 등
        drar_size: 굵기
        draw_fill: 그리기 채우기 판정
        draw_color: 그리기 색
        time_start: 그리기 시작
        time_end:   그리기 종료
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
