#  Copyright (c) by Konstantin Levickiy at 2023.
#

from .engine import Check


class IsLower(Check):
    """Проверка на условие если значение строчная буква"""
    verbose_name = "строчная буква"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.islower()


class IsUpper(Check):
    """Проверка на условие если значение заглавная буква"""
    verbose_name = "заглавная буква"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.isupper()


class Contains(Check):
    """Проверка на условие если значение содержится в строке"""
    verbose_name = "содержит"

    @staticmethod
    def check(check_value, value) -> bool:
        return check_value in value


class NotContains(Check):
    """Проверка на условие если значение не содержится в строке"""
    verbose_name = "не содержит"

    @staticmethod
    def check(check_value, value) -> bool:
        return check_value not in value


class StartsWith(Check):
    """Проверка на условие если значение начинается с"""
    verbose_name = "начинается с"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.startswith(check_value)


class NotStartsWith(Check):
    """Проверка на условие если значение не начинается с"""
    verbose_name = "не начинается с"

    @staticmethod
    def check(check_value, value) -> bool:
        return not value.startswith(check_value)


class EndsWith(Check):
    """Проверка на условие если значение заканчивается на"""
    verbose_name = "заканчивается на"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.endswith(check_value)


class NotEndsWith(Check):
    """Проверка на условие если значение не заканчивается на"""
    verbose_name = "не заканчивается на"

    @staticmethod
    def check(check_value, value) -> bool:
        return not value.endswith(check_value)


class ContainsIgnoreCase(Check):
    """Проверка на условие если значение содержит подстроку без учета регистра"""
    verbose_name = "содержит (без учета регистра)"

    @staticmethod
    def check(check_value, value) -> bool:
        return check_value.lower() in value.lower()


class StartsWithIgnoreCase(Check):
    """Проверка на условие если значение начинается с подстроки без учета регистра"""
    verbose_name = "начинается с (без учета регистра)"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.lower().startswith(check_value.lower())


class EndsWithIgnoreCase(Check):
    """Проверка на условие если значение заканчивается на подстроку без учета регистра"""
    verbose_name = "заканчивается на (без учета регистра)"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.lower().endswith(check_value.lower())