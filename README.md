# Lenin_Library

Задача
Команды, участвующие в хакатоне должны в качестве результата работы предоставить программные решения (группу отдельных программ или комплексный вариант),
который локализует и интерпретируют языковые конструкции в тексте. То есть превращает в машинночитаемую форму все фрагменты текста,
где речь идет о хоть сколько ни будь конкретном:

Моменте времени, который возможно привязать к стандартным календарям.
Отрезке времени между двумя моментами.
Временной протяженности события или периода.
Указания века, тысячелетия или их части
Решение задачи планируется в три этапа:

На первом этапе нужно будет обработать табличные записи,
заведомо содержащие временую конструкцию в виде текстовой строки.
В результате нужно првести ее к абсолютному значению в одном из 4
(упрощенных относительно специализированного формата) видов:
даты
даты + время
отрезку времени между двумя датами с точностью до 1 дня
отрезку времени между двумя датами с точностью до времени дня

Формат даты

Внимание!

Указывать секунды не нужно, как и их дробную часть и временную зону
Точка отсчета для всех относительных значений: 2020-11-27T2:30
Стандартные значения дат и времени задаются в формате ГОСТ Р 7.0.64-2018
"Система стандартов по информации, библиотечному и издательскому делу. Представление дат и времени. Общие требования" (модификация стандрта ISO 8601:2004)

Для указания временных значений используется расширенная (extended) форма нотации, если таковая описана для используемого типа временной отметки.

Для указания интервала используется разделитель в виде знака минус с двумя пробелами по бокам: -

Листинг приведен для второго этапа, который был облегчен - парсить год.
Программу можно использовать и для парсинга дат - для этого расскомментировать с 28 по 37 строку.
Распознование дат осуществлено при помощи библиотеки Natasha (https://github.com/natasha/natasha).
Программа писалась в https://colab.research.google.com/drive/1hmjN56ACXu_8UCzITxwnmxaPdMjrsMNR в команде с acarmela и mturquin.
Огромная благодарность trytolose, который помогал и направлял в ходе работы.

Результаты: https://www.kaggle.com/c/retropress-temporal-markup/leaderboard
