#  Copyright (c) by Konstantin Levickiy at 2023.
#

from .engine import Check
from datetime import datetime


class Data(Check):
    """Проверка на условие если значение дата"""
    verbose_name = "дата"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                return False

        return isinstance(value, datetime.date)


class Time(Check):
    """Проверка на условие если значение время"""
    verbose_name = "время"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%H:%M:%S')
            except ValueError:
                return False

        return isinstance(value, datetime.time)


class DateTime(Check):
    """Проверка на условие если значение дата и время"""
    verbose_name = "дата и время"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return False

        return isinstance(value, datetime)


class RangeDate(Check):
    """Проверка на условие если значение дата входит в диапазон"""
    verbose_name = "дата входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                return False

        return check_value[0] <= value <= check_value[1]


class RangeTime(Check):
    """Проверка на условие если значение время входит в диапазон"""
    verbose_name = "время входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%H:%M:%S')
            except ValueError:
                return False

        return check_value[0] <= value <= check_value[1]


class RangeDateTime(Check):
    """Проверка на условие если значение дата и время входит в диапазон"""
    verbose_name = "дата и время входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return False

        return check_value[0] <= value <= check_value[1]


class Year(Check):
    """Проверка на условие если значение год"""
    verbose_name = "год"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y')
            except ValueError:
                return False

        return isinstance(value, datetime.year)


class Month(Check):
    """Проверка на условие если значение месяц"""
    verbose_name = "месяц"

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%m')
            except ValueError:
                return False

        return isinstance(value, datetime.month)


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