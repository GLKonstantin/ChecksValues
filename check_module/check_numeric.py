#  Copyright (c) by Konstantin Levickiy at 2023.
#

from .engine import Check


class Greater(Check):
    """Проверка на условие если значение больше"""
    verbose_name = "больше"

    @staticmethod
    def check(check_value, value) -> bool:
        return value > check_value


class Less(Check):
    """Проверка на условие если значение меньше"""
    verbose_name = "меньше"

    @staticmethod
    def check(check_value, value) -> bool:
        return value < check_value


class GreaterEqual(Check):
    """Проверка на условие если значение больше или равно"""
    verbose_name = "больше или равно"

    @staticmethod
    def check(check_value, value) -> bool:
        return value >= check_value


class LessEqual(Check):
    """Проверка на условие если значение меньше или равно"""
    verbose_name = "меньше или равно"

    @staticmethod
    def check(check_value, value) -> bool:
        return value <= check_value


class IsFloat(Check):
    """Проверка на условие если значение число с плавающей точкой"""
    verbose_name = "число с плавающей точкой"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.replace('.', '', 1).isdigit()


class IsNotFloat(Check):
    """Проверка на условие если значение не число с плавающей точкой"""
    verbose_name = "не число с плавающей точкой"

    @staticmethod
    def check(check_value, value) -> bool:
        return not value.replace('.', '', 1).isdigit()


class IsInt(Check):
    """Проверка на условие если значение целое число"""
    verbose_name = "целое число"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.isdigit()


class IsNotInt(Check):
    """Проверка на условие если значение не целое число"""
    verbose_name = "не целое число"

    @staticmethod
    def check(check_value, value) -> bool:
        return not value.isdigit()


class Range(Check):
    """Проверка на условие если значение входит в диапазон"""
    verbose_name = "входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        return check_value[0] <= value <= check_value[1]


class NotRange(Check):
    """Проверка на условие если значение не входит в диапазон"""
    verbose_name = "не входит в диапазон"

    @staticmethod
    def check(check_value, value) -> bool:
        return not (check_value[0] <= value <= check_value[1])