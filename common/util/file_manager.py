from PySide6.QtWidgets import *
from common.util import notice


def file_open():
    full_path = QFileDialog.getOpenFileName(None, 'Open file', '/')

    file_path = f'{full_path[0]}'
    result = image_file_check(file_path)

    if result is None:
        notice.message('Warning', '이미지 파일을 선택을 하지 않았습니다. \n 지원 되는 형식은 jpg , png 입니다.')

    else:
        return result


def image_file_check(file_path: str):

    split_list = file_path.split('.')

    # 지원 형식
    extension = (['jpg', 'png'])

    # 마지막 인자의 교집합으로 확장자 확인 합니다.
    last_name =([split_list[-1]])
    intersection = list(set(extension) & set(last_name))
    count: int = len(intersection)

    if count == 0:
        return None
    else:
        return file_path