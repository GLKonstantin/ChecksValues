from .engine import Check
import re


class IsRegex(Check):
    """Проверка на условие если значение соответствует регулярному выражению"""
    verbose_name = "соответствует регулярному выражению"

    @staticmethod
    def check(check_value, value) -> bool:
        return bool(re.match(check_value, value))


class IsNotRegex(Check):
    """Проверка на условие если значение не соответствует регулярному выражению"""
    verbose_name = "не соответствует регулярному выражению"

    @staticmethod
    def check(check_value, value) -> bool:
        return not bool(re.match(check_value, value))


class RegexIgnoreCase(Check):
    """Проверка на условие если значение соответствует регулярному выражению без учета регистра"""
    verbose_name = "соответствует регулярному выражению (без учета регистра)"

    @staticmethod
    def check(check_value, value) -> bool:
        return re.match(check_value, value, re.IGNORECASE)


class NotRegexIgnoreCase(Check):
    """Проверка на условие если значение не соответствует регулярному выражению без учета регистра"""
    verbose_name = "не соответствует регулярному выражению (без учета регистра)"

    @staticmethod
    def check(check_value, value) -> bool:
        return not re.match(check_value, value, re.IGNORECASE)

