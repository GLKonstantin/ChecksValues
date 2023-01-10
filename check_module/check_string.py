#  Copyright (c) by Konstantin Levickiy at 2023.
#

from check_module.check import Check


class IsLower(Check):
    """Проверка на условие если значение строчная буква"""
    verbose_name = "строчная буква или слово"

    test_true = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        (None, 'd'),
        (None, 'e'),
        (None, 'fox'),
        (None, 'jump'),
        (None, 'over'),
        (None, 'яблоко'),
        (None, 'груша'),
        ]

    test_false = [
        (None, 'A'),
        (None, 'B'),
        (None, 'C'),
        (None, 'D'),
        (None, 'E'),
        (None, 'F'),
        (None, 'G'),
        (None, 'H'),
        (None, 'HARD'),
        (None, 'JUMP'),
        (None, 'OVER'),
        (None, 'Яблоко'),
        (None, 'Груша'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return value.islower()
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class IsUpper(Check):
    """Проверка на условие если значение заглавная буква"""
    verbose_name = "заглавная буква"

    test_true = [
        (None, 'A'),
        (None, 'B'),
        (None, 'C'),
        (None, 'D'),
        (None, 'E'),
        (None, 'F'),
        (None, 'G'),
        (None, 'H'),
        (None, 'HARD'),
        (None, 'JUMP'),
        (None, 'OVER'),
        (None, 'ЯБЛОКО'),
        (None, 'ГРУША'),
        ]

    test_false = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        (None, 'd'),
        (None, 'e'),
        (None, 'fox'),
        (None, 'jump'),
        (None, 'over'),
        (None, 'яблоко'),
        (None, 'груша'),
        (None, 'Яблоко'),
        (None, 'Груша'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return value.isupper()
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class Contains(Check):
    """Проверка на условие если значение содержится в строке"""
    verbose_name = "текст содержит"

    test_true = [
        ('a', 'a'),
        ('a', 'abc'),
        ('р', 'сарай'),
        ('ф', 'картофель'),
        ('П', 'СоПутствующий'),
        ]

    test_false = [
        ('a', 'b'),
        ('a', 'bc'),
        ('р', 'сало'),
        ('ф', 'картошка'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return check_value in value
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class NotContains(Check):
    """Проверка на условие если значение не содержится в строке"""
    verbose_name = "не содержит"

    test_true = [
        ('a', 'b'),
        ('a', 'bc'),
        ('р', 'сало'),
        ('ф', 'картошка'),
        ]

    test_false = [
        ('a', 'a'),
        ('a', 'abc'),
        ('р', 'сарай'),
        ('ф', 'картофель'),
        ('п', 'Сопутствующий'),
        ('V', 'COVID-19'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return check_value not in value
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class StartsWith(Check):
    """Проверка на условие если значение начинается с"""
    verbose_name = "текст начинается с"

    test_true = [
        ('a', 'abc'),
        ('сар', 'сарай'),
        ('кар', 'картофель'),
        ('Соп', 'Сопутствующий'),
        ('COVID', 'COVID-19'),
        ('D:', r'D:/My Documents/'),
        ]

    test_false = [
        ('a', 'ba'),
        ('a', 'bca'),
        ('ало', 'сало'),
        ('D:', r'F:\My Documents\My Music'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return value.startswith(check_value)
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class NotStartsWith(Check):
    """Проверка на условие если значение не начинается с"""
    verbose_name = "не начинается с"

    test_true = [
        ('a', 'ba'),
        ('a', 'bca'),
        ('ало', 'сало'),
        ('D:', r'F:\My Documents\My Music'),
        ]

    test_false = [
        ('a', 'abc'),
        ('сар', 'сарай'),
        ('кар', 'картофель'),
        ('Соп', 'Сопутствующий'),
        ('COVID', 'COVID-19'),
        ('D:', r'D:/My Documents/'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return not value.startswith(check_value)
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class EndsWith(Check):
    """Проверка на условие если значение заканчивается на"""
    verbose_name = "заканчивается на"

    test_true = [
        ('a', 'ba'),
        ('a', 'bca'),
        ('ло', 'сало'),
        ('My Music', r'F:\My Documents\My Music'),
        ]

    test_false = [
        ('a', 'abc'),
        ('сар', 'сарай'),
        ('кар', 'картофель'),
        ('Соп', 'Сопутствующий'),
        ('COVID', 'COVID-19'),
        ('D:', r'D:/My Documents/'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return value.endswith(check_value)
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class NotEndsWith(Check):
    """Проверка на условие если значение не заканчивается на"""
    verbose_name = "текст не заканчивается на"

    test_true = [
        ('a', 'abc'),
        ('сар', 'сарай'),
        ('кар', 'картофель'),
        ('Соп', 'Сопутствующий'),
        ('COVID', 'COVID-19'),
        ('D:', r'D:/My Documents/'),
        ]

    test_false = [
        ('a', 'ba'),
        ('a', 'bca'),
        ('ло', 'сало'),
        ('My Music', r'F:\My Documents\My Music'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return not value.endswith(check_value)
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class ContainsIgnoreCase(Check):
    """Проверка на условие если значение содержит подстроку без учета регистра"""
    verbose_name = "содержит (без учета регистра)"

    test_true = [
        ('B', 'abc'),
        ('аРа', 'сарай'),
        ('ТОФ', 'картофель'),
        ('FOX', 'foxtrot'),
        ('COVID', 'COVID-19'),
        ('COVID', 'covid-19'),
        ('d:', r'D:/My Documents/'),
        ]

    test_false = [
        ('f', 'abc'),
        ('кар', 'сарай'),
        ('сар', 'картофель'),
        ('FOX', 'modernization'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return check_value.lower() in value.lower()
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class StartsWithIgnoreCase(Check):
    """Проверка на условие если значение начинается с подстроки без учета регистра"""
    verbose_name = "начинается с (без учета регистра)"

    test_true = [
        ('A', 'abc'),
        ('a', 'abstract'),
        ('сА', 'сарай'),
        ('КАР', 'картофель'),
        ('FOX', 'foxtrot'),
        ('COVID', 'COVID-19'),
        ('COVID', 'covid-19'),
        ('d:', r'D:/My Documents/'),
        ]

    test_false = [
        ('a', 'ba'),
        ('a', 'bca'),
        ('ло', 'сало'),
        ('My Music', r'F:\My Documents\My Music'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return value.lower().startswith(check_value.lower())
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')


class EndsWithIgnoreCase(Check):
    """Проверка на условие если значение заканчивается на подстроку без учета регистра"""
    verbose_name = "заканчивается на (без учета регистра)"

    test_true = [
        ('C', 'abc'),
        ('T', 'abstract'),
        ('й', 'сарай'),
        ('ЕЛЬ', 'картофель'),
        ('ROT', 'foxtrot'),
        ('19', 'COVID-19'),
        ('d-19', 'covid-19'),
        ('/', r'D:/My Documents/'),
        ]

    test_false = [
        ('b', 'ba'),
        ('c', 'bca'),
        ('са', 'сало'),
        ('/', r'F:\My Documents\My Music'),
        ]

    test_exception = [
        (None, 1),
        (None, ()),
        (None, []),
        (None, {}),
        (None, True),
        (None, False),
        (None, None),
        (1, 'a'),
        ((), 'a'),
        ([], 'a'),
        ({}, 'a'),
        (True, 'a'),
        (False, 'a'),
        ('a', 1),
        ('a', ()),
        ('a', []),
        ('a', {}),
        ('a', True),
        ('a', False),
        ('a', None),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and isinstance(value, str):
            return value.lower().endswith(check_value.lower())
        else:
            raise TypeError(f'Значение должно быть строкой а не {type(value)}')