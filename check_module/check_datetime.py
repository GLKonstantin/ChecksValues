#  Copyright (c) by Konstantin Levickiy at 2023.
#

from check_module.check import CheckConditions
import datetime
from check_module.check_utils import (
    get_date_from_string,
    get_time_from_string,
    get_datetime_from_string,
    MONTHS,
    WEEKDAYS,
)


class IsData(CheckConditions):
    """Проверка на условие если значение дата"""
    verbose_name = "дата"

    test_true = [
        ('', '2020-01-01'),
        ('', '2020/01/01'),
        ('', '2020.01.02'),
        ('', '01-01-2020'),
        ('', '01.01.2020'),
        ('', '01/01/2020'),
        ('', '01.01.2020 12:00:00'),
        ('', datetime.datetime.now()),
    ]

    test_false = [
        ('', 'TestFalse'),
        ('', 1),
        ('', 1.1),
        ('', True),
        ('', None),
        ('', '2020-01-32 00:00:00'),
        ('', '2020/13/01 00:00:00'),
        ('', '2020.01'),
        ('', '32-01-2020'),
        ('', '01.13.2020'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        """Проверка на условие если значение дата"""

        if isinstance(value, str):
            value = get_date_from_string(value)

        return isinstance(value, datetime.date)


class IsTime(CheckConditions):
    """Проверка на условие если значение время"""
    verbose_name = "время"

    test_true = [
        ('', '00:01:51'),
        ('', '00.02.10'),
        ('', '00-03-20'),
        ('', '00:04:30:405485'),
        ('', datetime.datetime.now()),
        ('', datetime.datetime.now().time()),
    ]

    test_false = [
        ('', 'TestFalse'),
        ('', 1),
        ('', 1.1),
        ('', True),
        ('', None),
        ('', '00:01:61'),
        ('', '00.02.70'),
        ('', '00-03-80'),
        ('', '00:04:30:405485:405485'),
        ('', '2020-01-32 00:00:00'),
        ('', '2020/13/01 00:00:00'),
        ('', '2020.01'),
        ('', '30-01-2020'),
        ('', '01.10.2020'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        """Проверка на условие если значение время"""
        if isinstance(value, str):
            value = get_time_from_string(value)

        if isinstance(value, datetime.datetime):
            value = value.time()

        return isinstance(value, datetime.time)


class IsDateTime(CheckConditions):
    """Проверка на условие если значение дата и время"""
    verbose_name = "дата и время"

    test_true = [
        ('', '2020-01-01 00:01:51'),
        ('', '2020/01/01 00.02.10'),
        ('', '2020.01.02 00-03-20'),
        ('', '01-01-2020 00:04:30:405485'),
        ('', '01.01.2020 00:04:30:405485'),
        ('', '01/01/2020 00:04:30:405485'),
        ('', datetime.datetime.now()),
    ]

    test_false = [
        ('', 'TestFalse'),
        ('', 1),
        ('', 1.1),
        ('', True),
        ('', None),
        ('', '2020-01-32 00:00:00'),
        ('', '2020/13/01 00:00:00'),
        ('', '2020.01'),
        ('', '32-01-2020'),
        ('', '01.13.2020'),
        ('', '00:01:61'),
        ('', '00.02.70'),
        ('', '00-03-80'),
        ('', '00:04:30:405485:405485'),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        """Проверка на условие если значение дата и время"""
        if isinstance(value, str):
            value = get_datetime_from_string(value)

        return isinstance(value, datetime.datetime)


class RangeDate(CheckConditions):
    """Проверка на условие если значение дата входит в диапазон"""
    verbose_name = "дата входит в диапазон"

    test_true = [
        ('2020-01-01', ('2019-01-01', '2020-01-01')),
        ('2020.01.01', ('2019.01.01', '2020.01.02')),
        ('2020/01/01', ('2019/01/01', '2020/01/02')),
        ('01-01-2020', ('01-01-2019', '01-01-2020')),
        ('01.01.2020', ('01.01.2019', '01.01.2020')),
        ('01/01/2020', ('01/01/2019', '01/01/2020')),
        ('15/01/2020', ('13/01/2019', '16/01/2020')),
        ('15/01/2020', ('13/01/2019', '15/01/2020')),
        ('15/01/2020', ('15/01/2019', '15/01/2020')),
        ('15/01/2020', ('13/01/2020', '15/01/2020')),
        ('01.01.2020 12:00:00', ('01.01.2019 12:00:00', '01.01.2020 12:00:00')),
        (datetime.datetime.now(), (datetime.datetime.now() - datetime.timedelta(days=1), datetime.datetime.now())),
    ]

    test_false = [
        ('2020-01-01', ('2019-01-01', '2019-01-01')),
        ('2020.01.15', ('2020.01.01', '2019.01.02')),
        ('2020/01/15', ('2020/01/01', '2019/01/02')),
        ('15-01-2020', ('01-01-2019', '01-01-2019')),
        ('15.01.2020', ('01.01.2019', '01.01.2019')),
        ('15/01/2020', ('01/01/2019', '01/01/2019')),
        ('15/01/2020', ('13/01/2019', '14/01/2020')),
        ('15/01/2020', ('13/01/2019', '14/01/2020')),
        ('15/01/2020', ('13/01/2020', '14/01/2020')),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        """Проверка на условие если значение дата входит в диапазон"""
        if not isinstance(value, (list, tuple)):
            raise ValueError(f'Значение "value" должно быть списком а не {type(value)}')

        # проверить что в списке 2 значения
        if len(value) != 2:
            raise ValueError(f'Значение "value" должно быть списком из 2 элементов а не из {len(value)}')

        # Проверка на то что все значения в списке являются датами
        if not all([isinstance(get_date_from_string(v), datetime.date) for v in value]):
            raise ValueError(f'Значение "value" должно быть списком дат')

        if isinstance(check_value, str):
            check_value = get_date_from_string(check_value)

        value = [get_date_from_string(v) for v in value]

        # Проверка на то что дата входит в диапазон
        return value[0] <= check_value <= value[1]


class RangeTime(CheckConditions):
    """Проверка на условие если значение время входит в диапазон"""
    verbose_name = "время входит в диапазон"

    test_true = [
        ('12:00:00', ('11:00:00', '12:00:00')),
        ('12:00:00', ('11:00:00', '13:00:00')),
        ('12.00.00', ('11.00.00', '12.00.00')),
        ('12.00.00', ('11.00.00', '13.00.00')),
        ('12:00:00.100000', ('12:00:00.90000', '12:00:00.110000')),
        ('12.00.00.100000', ('12.00.00.90000', '12.00.00.100000')),
        ]

    test_false = [
        ('12:00:00', ('11:00:00', '11:00:00')),
        ('12:00:00', ('13:00:00', '13:00:00')),
        ('12.00.00', ('11.00.00', '11.00.00')),
        ('12.00.00', ('13.00.00', '13.00.00')),
        ('12:00:00.100000', ('12:00:00.90000', '12:00:00.099999')),
        ('12.00.00.100000', ('12.00.00.90000', '12.00.00.099999')),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        """Проверка на условие если значение время входит в диапазон"""
        if not isinstance(value, (list, tuple)):
            raise ValueError(f'Значение "value" должно быть списком а не {type(value)}')

        # проверить что в списке 2 значения
        if len(value) != 2:
            raise ValueError(f'Значение "value" должно быть списком из 2 элементов а не из {len(value)}')

        value = [get_time_from_string(v) for v in value]

        # Проверка на то что все значения в списке являются временем
        if not all([isinstance(v, datetime.time) for v in value]):

            raise ValueError(
                f'Значение "value" должно быть списком из времени формата "HH:MM:SS" или datetime '
                f'а не из {value}'
            )

        if isinstance(check_value, str):
            check_value = get_time_from_string(check_value)

        # Проверка на то что время входит в диапазон
        return value[0] <= check_value <= value[1]


class RangeDateTime(CheckConditions):
    """Проверка на условие если значение дата и время входит в диапазон"""
    verbose_name = "дата и время входит в диапазон"

    test_true = [
        ('2020-01-15 12:00:00', ('2020-01-15 11:00:00', '2020-01-15 12:00:00')),
        ('2020-01-15 12:00:00', ('2020-01-14 11:00:00', '2020-01-15 12:00:00')),
        ('2020-01-15 12:00:00', ('2020-01-15 11:00:00', '2020-01-16 12:00:00')),
        ('2020-01-15 12:00:00', ('2020-01-14 11:00:00', '2020-01-16 12:00:00')),
        ('2020-01-15 12:00:00.100000', ('2020-01-15 11:00:00.90000', '2020-01-15 12:00:00.110000')),
        ('2020.01.15 12.00.00', ('2020.01.15 11.00.00', '2020.01.15 12.00.00')),
        ('2020.01.15 12.00.00', ('2020.01.14 11.00.00', '2020.01.15 12.00.00')),
        ('2020.01.15 12.00.00', ('2020.01.15 11.00.00', '2020.01.16 12.00.00')),
        ('2020.01.15 12.00.00', ('2020.01.14 11.00.00', '2020.01.16 12.00.00')),
        ('2020.01.15 12.00.00.100000', ('2020.01.15 11.00.00.90000', '2020.01.15 12.00.00.100000')),
        ('2020.01.15 12.00.00.100000', ('2020.01.13 11.00.00.90000', '2020.01.16 12.00.00.100000')),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        """Проверка на условие если значение дата и время входит в диапазон"""
        if not isinstance(value, (list, tuple)):
            raise ValueError(f'Значение "value" должно быть списком а не {type(value)}')

        # проверить что в списке 2 значения
        if len(value) != 2:
            raise ValueError(f'Значение "value" должно быть списком из 2 элементов а не из {len(value)}')

        value = [get_datetime_from_string(v) for v in value]

        # Проверка на то что все значения в списке являются датой и временем
        if not all([isinstance(v, datetime.datetime) for v in value]):

            raise ValueError(
                f'Значение "value" должно быть списком из даты и времени формата "YYYY-MM-DD HH:MM:SS" или '
                f'datetime а не из {value}'
            )

        if isinstance(check_value, str):
            check_value = get_datetime_from_string(check_value)

        # Проверка на то что дата и время входит в диапазон
        return value[0] <= check_value <= value[1]


class Year(CheckConditions):
    """Проверка на условие если значение год"""
    verbose_name = "год"

    test_true = [
        ('_', 2020),
        ('_', '2021'),
        ('_', '2022'),
        ('_', '2023'),
        ('_', 1999),
        ('_', '2024'),
        ('_', '1950'),
    ]

    test_false = [
        ('_', '20202'),
        ('_', '20'),
        ('_', '202'),
        ('_', 20202),
        ('_', 20),
        ('_', 202),
    ]

    test_exception = [
        ('_', '2020.01.01 12:00:00'),
        ('_', '2020.1'),
        ('_', '2020.01'),
        ('_', '2020.01.01'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        """Проверка на условие если значение год"""
        if not isinstance(value, (str, int)):
            print(type(value))
            raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {type(value)}')

        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {value}')
        if value < 1900 or value > 2100:
            return False
        value = datetime.datetime(value, 1, 1)
        return isinstance(value, datetime.datetime)


class Month(CheckConditions):
    """Проверка на условие если значение месяц"""
    verbose_name = "месяц"

    test_true = [
        ('_', 1),
        ('_', 2),
        ('_', 3),
        ('_', 4),
        ('_', 5),
        ('_', 6),
        ('_', 7),
        ('_', 8),
        ('_', 9),
        ('_', 10),
        ('_', 11),
        ('_', 12),
        ('_', '01'),
        ('_', '02'),
        ('_', '03'),
        ('_', '04'),
        ('_', '05'),
        ('_', '06'),
        ('_', '07'),
        ('_', '08'),
        ('_', '09'),
        ('_', '10'),
        ('_', '11'),
        ('_', '12'),
        ('_', 'Январь'),
        ('_', 'Февраль'),
        ('_', 'Март'),
        ('_', 'Апрель'),
        ('_', 'Май'),
        ('_', 'Июнь'),
        ('_', 'Июль'),
        ('_', 'Август'),
        ('_', 'Сентябрь'),
        ('_', 'Октябрь'),
        ('_', 'Ноябрь'),
        ('_', 'Декабрь'),
        ('_', 'january'),
        ('_', 'february'),
        ('_', 'march'),
        ('_', 'april'),
        ('_', 'may'),
        ('_', 'june'),
        ('_', 'july'),
        ('_', 'august'),
        ('_', 'september'),
        ('_', 'october'),
        ('_', 'november'),
        ('_', 'december'),
        ('_', 'jan'),
        ('_', 'feb'),
        ('_', 'mar'),
        ('_', 'apr'),
        ('_', 'may'),
        ('_', 'jun'),
        ('_', 'jul'),
        ('_', 'aug'),
        ('_', 'sep'),
        ('_', 'oct'),
        ('_', 'nov'),
        ('_', 'dec'),
        ('_', 'января'),
        ('_', 'февраля'),
        ('_', 'марта'),
        ('_', 'апреля'),
        ('_', 'мая'),
        ('_', 'июня'),
        ('_', 'июля'),
        ('_', 'августа'),
        ('_', 'сентября'),
        ('_', 'октября'),
        ('_', 'ноября'),
        ('_', 'декабря'),
    ]

    test_false = [
        ('_', '13'),
        ('_', '0'),
        ('_', '1.1'),
        ('_', '1.01'),
        ('_', 'ABRAKADABRA'),
        ('_', 'ян'),
        ('_', 13),
        ('_', 0),
        ]

    test_exception = [
        ('_', 1.1),
        ('_', (1, 1)),
        ('_', [1, 1]),
        ('_', {'1': 1}),
        ('_', None),
        ('_', True),
        ('_', False),
        ('_', 1j),
        ('_', 1+1j),
        ('_', 1j+1),
    ]

    @staticmethod
    def check(_, value) -> bool:
        """Проверка на условие если значение месяц"""
        if not isinstance(value, (str, int)):
            raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {type(value)}')

        if isinstance(value, str):
            if value.isdigit():
                value = int(value)
            else:
                value = value.lower()
                if value in MONTHS:
                    value = MONTHS.get(value)
                else:
                    return False

        if value < 1 or value > 12:
            return False
        value = datetime.datetime(2020, value, 1)
        return isinstance(value, datetime.date)


class Day(CheckConditions):
    """Проверка на условие если значение день"""
    verbose_name = "день"

    test_true = [
        ('_', 1),
        ('_', 2),
        ('_', 3),
        ('_', 4),
        ('_', 5),
        ('_', 6),
        ('_', 7),
        ('_', 8),
        ('_', 9),
        ('_', 10),
        ('_', 11),
        ('_', 12),
        ('_', 13),
        ('_', 14),
        ('_', 15),
        ('_', 16),
        ('_', 17),
        ('_', 18),
        ('_', 19),
        ('_', 20),
        ('_', 21),
        ('_', 22),
        ('_', 23),
        ('_', 24),
        ('_', 25),
        ('_', 26),
        ('_', 27),
        ('_', 28),
        ('_', 29),
        ('_', 30),
        ('_', 31),
        ('_', '01'),
        ('_', '02'),
        ('_', '03'),
        ('_', '04'),
        ('_', '05'),
        ('_', '06'),
        ('_', '07'),
        ('_', '08'),
        ('_', '09'),
        ('_', '10'),
        ('_', '11'),
        ('_', '12'),
        ('_', '13'),
        ('_', '14'),
        ('_', '15'),
        ('_', '16'),
        ('_', '17'),
        ('_', '18'),
        ('_', '19'),
        ('_', '20'),
        ('_', '21'),
        ('_', '22'),
        ('_', '23'),
        ('_', '24'),
        ('_', '25'),
        ('_', '26'),
        ('_', '27'),
        ('_', '28'),
        ('_', '29'),
        ('_', '30'),
        ('_', '31'),

    ]

    test_false = [
        ('_', '32'),
        ('_', '0'),
        ('_', '1.1'),
        ('_', '1.01'),
        ('_', 'ABRAKADABRA'),
        ('_', 32),
        ('_', 0),
        ]

    test_exception = [
        ('_', 1.1),
        ('_', (1, 1)),
        ('_', [1, 1]),
        ('_', {'1': 1}),
        ('_', None),
        ('_', True),
        ('_', False),
        ('_', 1j),
        ('_', 1+1j),
        ('_', 1j+1),
        ]

    @staticmethod
    def check(_, value) -> bool:
        """Проверка на условие если значение день"""
        if not isinstance(value, (str, int)):
            raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {type(value)}')

        if isinstance(value, str):
            if value.isdigit():
                value = int(value)
            else:
                return False

        if value < 1 or value > 31:
            return False
        value = datetime.datetime(2020, 1, value)
        return isinstance(value, datetime.date)


class WeekDay(CheckConditions):
    """Проверка на условие если значение день недели"""
    verbose_name = "день недели"

    test_true = [
        ('_', 1),
        ('_', 2),
        ('_', 3),
        ('_', 4),
        ('_', 5),
        ('_', 6),
        ('_', 7),
        ('_', '1'),
        ('_', '2'),
        ('_', '3'),
        ('_', '4'),
        ('_', '5'),
        ('_', '6'),
        ('_', '7'),
        ('_', 'понедельник'),
        ('_', 'вторник'),
        ('_', 'среда'),
        ('_', 'четверг'),
        ('_', 'пятница'),
        ('_', 'суббота'),
        ('_', 'воскресенье'),
        ('_', 'пн'),
        ('_', 'вт'),
        ('_', 'ср'),
        ('_', 'чт'),
        ('_', 'пт'),
        ('_', 'сб'),
        ('_', 'вс'),
        ('_', 'ПН'),
        ('_', 'ВТ'),
        ('_', 'СР'),
        ('_', 'ЧТ'),
        ('_', 'ПТ'),
        ('_', 'СБ'),
        ('_', 'ВС'),
        ('_', 'Пн'),
        ('_', 'Вт'),
        ('_', 'Ср'),
        ('_', 'Чт'),
        ('_', 'Пт'),
        ('_', 'Сб'),
        ('_', 'Вс'),
        ('_', 'пН'),
        ('_', 'вТ'),
        ('_', 'сР'),
        ('_', 'чТ'),
        ('_', 'пТ'),
        ('_', 'сБ'),
        ('_', 'вС'),
        ('_', 'ПонЕдЕлЬник'),
        ('_', 'ВтОрНик'),
        ('_', 'СрЕдА'),
        ('_', 'ЧетВеРг'),
        ('_', 'ПятНиЦа'),
        ('_', 'СУбБота'),
        ('_', 'ВОскРеСеНьЕ'),
        ('_', 'ПОНЕДЕЛЬНИК'),
        ('_', 'ВТОРНИК'),
        ('_', 'СРЕДА'),
        ('_', 'ЧЕТВЕРГ'),
        ('_', 'ПЯТНИЦА'),
        ('_', 'СУББОТА'),
        ('_', 'ВОСКРЕСЕНЬЕ'),
        ('_', 'Monday'),
        ('_', 'Tuesday'),
        ('_', 'Wednesday'),
        ('_', 'Thursday'),
        ('_', 'Friday'),
        ('_', 'Saturday'),
        ('_', 'Sunday'),
        ('_', 'MONDAY'),
        ('_', 'TUESDAY'),
        ('_', 'WEDNESDAY'),
        ('_', 'THURSDAY'),
        ('_', 'FRIDAY'),
        ('_', 'SATURDAY'),
        ('_', 'SUNDAY'),
        ('_', 'monday'),
        ('_', 'tuesday'),
        ('_', 'wednesday'),
        ('_', 'thursday'),
        ('_', 'friday'),
        ('_', 'saturday'),
        ('_', 'sunday'),
        ('_', 'MON'),
        ('_', 'TUE'),
        ('_', 'WED'),
        ('_', 'THU'),
        ('_', 'FRI'),
        ('_', 'SAT'),
        ('_', 'SUN'),
        ('_', 'Mon'),
        ('_', 'Tue'),
        ('_', 'Wed'),
        ('_', 'Thu'),
        ('_', 'Fri'),
        ('_', 'Sat'),
        ('_', 'Sun'),
        ('_', 'mon'),
        ('_', 'tue'),
        ('_', 'wed'),
        ('_', 'thu'),
        ('_', 'fri'),
        ('_', 'sat'),
        ('_', 'sun'),
        ('_', 'monday'),
        ('_', 'tuesday'),
        ('_', 'wednesday'),
        ('_', 'thursday'),
        ('_', 'friday'),
        ('_', 'saturday'),
        ('_', 'sunday'),
        ]

    test_false = [
        ('_', 0),
        ('_', 15),
        ('_', '0'),
        ('_', '15'),
        ('_', 'Груша'),
    ]

    test_exception = [
        ('_', None),
        ('_', True),
        ('_', False),
        ('_', 1.1),
        ('_', '1.1'),
        ('_', (1, 1,)),
        ('_', [1, 1]),
        ('_', {1: 1}),
        ('_', {1, 1}),
        ('_', object()),
        ('_', lambda x: x),
        ('_', type),
    ]

    @staticmethod
    def check(_, value: str or int) -> bool:
        """Проверка на условие если значение день недели"""
        if not isinstance(value, (str, int)):
            raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {type(value)}')

        if isinstance(value, str):
            if value.lower() in WEEKDAYS:
                return True

            if value.isdigit():
                value = int(value)
            else:
                return False

        if value < 1 or value > 7:
            return False

        return True
