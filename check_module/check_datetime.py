#  Copyright (c) by Konstantin Levickiy at 2023.
#

from .engine import Check
import datetime
from check_module.check_utils import (
    get_date_from_string,
    get_time_from_string,
    get_datetime_from_string,

)


class IsData(Check):
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


class IsTime(Check):
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


class DateTime(Check):
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


class RangeDate(Check):
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


class RangeTime(Check):
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


class RangeDateTime(Check):
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


class Year(Check):
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


MONTHS = {
            'Январь': 1,
            'Февраль': 2,
            'Март': 3,
            'Апрель': 4,
            'Май': 5,
            'Июнь': 6,
            'Июль': 7,
            'Август': 8,
            'Сентябрь': 9,
            'Октябрь': 10,
            'Ноябрь': 11,
            'Декабрь': 12,
            'january': 1,
            'february': 2,
            'march': 3,
            'april': 4,
            'may': 5,
            'june': 6,
            'july': 7,
            'august': 8,
            'september': 9,
            'october': 10,
            'november': 11,
            'december': 12,
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12,
        }


class Month(Check):
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
                    raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {value}')
            # raise ValueError(f'Значение "value" должно быть целым числом или строкой а не {value}')

        if value < 1 or value > 12:
            return False
        value = datetime.datetime(2020, value, 1)
        return isinstance(value, datetime.datetime)


class Day(Check):
    """Проверка на условие если значение день"""
    verbose_name = "день"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%d')
            except ValueError:
                return False

        return isinstance(value, datetime.day)


class WeekDay(Check):
    """Проверка на условие если значение день недели"""
    verbose_name = "день недели"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%w')
            except ValueError:
                return False

        return isinstance(value, datetime.weekday)


class Hour(Check):
    """Проверка на условие если значение час"""
    verbose_name = "час"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%H')
            except ValueError:
                return False

        return isinstance(value, datetime.hour)


class Minute(Check):
    """Проверка на условие если значение минута"""
    verbose_name = "минута"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%M')
            except ValueError:
                return False

        return isinstance(value, datetime.minute)


class Second(Check):
    """Проверка на условие если значение секунда"""
    verbose_name = "секунда"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%S')
            except ValueError:
                return False

        return isinstance(value, datetime.second)


class DateRange(Check):
    """Проверка на условие если значение дата входит в диапазон дат"""
    verbose_name = "дата входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                return False

        return check_value[0] <= value <= check_value[1]


class DateTimeRange(Check):
    """Проверка на условие если значение дата и время входит в диапазон дат"""
    verbose_name = "дата и время входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return False

        return check_value[0] <= value <= check_value[1]


class TimeRange(Check):
    """Проверка на условие если значение время входит в диапазон дат"""
    verbose_name = "время входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%H:%M:%S')
            except ValueError:
                return False

        return check_value[0] <= value <= check_value[1]