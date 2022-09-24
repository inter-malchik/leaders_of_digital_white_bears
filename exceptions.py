import exception_window


class format_photo_exception(Exception):
    def __init__(self, file_path):
        _message = f"Изображение {file_path} преобразовано в формат jpg"
        exception_window.throw_warning_window(_message, 'Предупреждение')

class folder_data(Exception):
    def __init__(self, folder_path):
        _message = f"Папка {folder_path} содержит не допустимые форматы данных.\n" \
                   f"Возможно папка {folder_path} содержит другие папки или файлы, которые не являются изображениями\"" \
                   f"форматов .png и .bmp"
        exception_window.throw_error_window(_message, 'Ошибка выполнения')
