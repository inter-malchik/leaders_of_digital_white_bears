# leaders_of_digital_white_bears

Участникам предстоит на основе представленных данных аэрофотосъемки, сформированных датасетов и материалов из открытых источников обучить нейросеть поиску белых медведей, а также сформировать интерфейс загрузки данных и представления результатов распознавания с учетом требования по автономности решения (без использования сети «Интернет»). 

----------------------------------------------

Распознавание белых медведей в Арктике на основании аэрофотосъемки — трудозатратная задача, учитывая площади аэрофотосъемки и особенности местности (белый медведь на белом снегу). Основная сложность задачи заключается в малом объеме выборки с объектами. Фотографии аэрофотосъемки с медведями в Арктике получить сложно. При подобной съемке собирается большое количество пустых фотографий, среди которых лишь незначительное число содержит объект поиска. 

----------------------------------------------

# ИСИТОВЦЫ ПРЕЗИДЕНТЫ МИРА

Решение:
Сверточная нейронная сеть
 
Обученная модель Yolov7 с 3 сотнями эпох, помогает с точностью 0,9 определять полярного медведя по новый снимкам с аэрофотосъемки
 
В комбинации с простым интерфейсом Desktop-приложения, помогает производить детекцию белых медведей по фото любому пользователю ПК.
 
 
стек:
PyThorch
LabelIMg
YoloV7
 
Особенности:
Обучение было произведено на разных классах объектов (медведи из интернета, и, медведи со снимков аэрофотосъемки)
 
Дополнительная выборка была сформирована и размечена вручную
 
Использовались разные масштабы/тональности фотографий
 
В планах обучить YoloV7 Large - в погоня за повышением скора
 
----------------------------------------------
 
Desktop-приложение - утилита для поиска белых медведей на основе данных аэрофотосъемки
 
Функционал:
загрузка директории с данными аэрофотосъемки,
возможность просмотра и ревью результатов разпознавания изображения
 
Стек решения:
Python
PyQt5
Pillow
 
Уникальность: 
Возможность провести ревью результатов анализа изображений. Пользователь вправе удалить ошибочные данные.
 
Юзер-френдли интерфейс. 
Утилита сама переведет изображения в нужный формат. 
Всплывающие окна (при ошибках) помогут пользователю правильно взаимодействовать с интерфейсом.
 
Удобство.
Утилита самостоятельно выберет фрагменты с белыми медведями на фотоснимке
 
Информативность
В каждый анализированный утилитой снимок будет добавлен фрагмент с метаданными: 
Дата аэрофотосъемки, 
Дата анализа снимка, 
Директория, из которой был загружен снимок
 
Кроссплатформенность
Стек позволяет собрать приложение на любую операционную систему, поддерживающую интерпретатор Python 3.
 
Минимальные технические требования:
 
Windows 8 64bit или новее, Mac OS X или новее, Linux - индивидуально
Минимум 4 гб RAM
Минимум 5-10 ГБ свободного места на HDD/SSD (в момент использования - в зависимости от величины анализируемой выборки)


