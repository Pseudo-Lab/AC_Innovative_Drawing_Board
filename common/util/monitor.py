
import ctypes

# 모니터 화면 사이즈
def get_size():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    f'{screen_width}, {screen_height}'
    return screen_width, screen_height
