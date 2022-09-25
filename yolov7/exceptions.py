import exception_window


class format_photo_exception(Exception):
    def __init__(self, file_path):
        _message = f"Изображение {file_path} преобразовано в формат JPG"
        exception_window.throw_warning_window(_message, 'Предупреждение')

class folder_data(Exception):
    def __init__(self, folder_path):
        _message = f"Папка {folder_path} содержит не допустимые форматы данных.\n" \
                   f"Возможно папка {folder_path} содержит другие папки или файлы, которые не являются изображениями\"" \
                   f"форматов .png, .bmp и .jpg"
        exception_window.throw_error_window(_message, 'Ошибка выполнения')

class cant_convert_file_to_jpg(Exception):
    def __init__(self, file_path):
        _message = f"Файл {file_path} не может быть конвертирован в JPG.\n" \
                   f"Вы можете удалить этот файл и запустить обработку заново."
        exception_window.throw_error_window(_message, 'Ошибка конвертации данных')