#  Copyright (c) by Konstantin Levickiy at 2023.
#

from check_module.engine import Check


class Greater(Check):
    """Проверка на условие если значение больше"""
    verbose_name = "больше"

    test_true = [
        (1, 0),
        (2, 1.5),
        (3, 2.5),
        (100, 50),
        (100, 99),
    ]

    test_false = [
        (0, 1),
        (1.5, 2),
        (2.5, 3),
        (50, 100),
        (99, 100),
        (100, 100),
    ]

    test_exception = [
        (1, 'a'),
        ('a', 1),
        ('a', 'b'),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, (int, float)) and isinstance(value, (int, float)):
            return check_value > value
        else:
            raise TypeError(f"Данные не являются числами: {type(check_value)}, {type(value)}")


class Less(Check):
    """Проверка на условие если значение меньше"""
    verbose_name = "меньше"

    test_true = [
        (0, 1),
        (1.5, 2),
        (2.5, 3),
        (50, 100),
        (99, 100),
    ]

    test_false = [
        (1, 0),
        (2, 1.5),
        (3, 2.5),
        (100, 50),
        (100, 99),
        (100, 100),
    ]

    test_exception = [
        (1, 'a'),
        ('a', 1),
        ('a', 'b'),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, (int, float)) and isinstance(value, (int, float)):
            return check_value < value
        else:
            raise TypeError(f"Данные не являются числами: {type(check_value)}, {type(value)}")


class GreaterEqual(Check):
    """Проверка на условие если значение больше или равно"""
    verbose_name = "больше или равно"

    test_true = [
        (1, 0),
        (2, 1.5),
        (3, 2.5),
        (100, 50),
        (100, 99),
        (100, 100),
    ]

    test_false = [
        (0, 1),
        (1.5, 2),
        (2.5, 3),
        (50, 100),
        (99, 100),
    ]

    test_exception = [
        (1, 'a'),
        ('a', 1),
        ('a', 'b'),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, (int, float)) and isinstance(value, (int, float)):
            return check_value >= value
        else:
            raise TypeError(f"Данные не являются числами: {type(check_value)}, {type(value)}")


class LessEqual(Check):
    """Проверка на условие если значение меньше или равно"""
    verbose_name = "меньше или равно"

    test_true = [
        (0, 1),
        (1.5, 2),
        (2.5, 3),
        (50, 100),
        (99, 100),
        (100, 100),
    ]

    test_false = [
        (1, 0),
        (2, 1.5),
        (3, 2.5),
        (100, 50),
        (100, 99),
    ]

    test_exception = [
        (1, 'a'),
        ('a', 1),
        ('a', 'b'),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, (int, float)) and isinstance(value, (int, float)):
            return check_value <= value
        else:
            raise TypeError(f"Данные не являются числами: {type(check_value)}, {type(value)}")


class IsFloat(Check):
    """Проверка на условие если значение число с плавающей точкой"""
    verbose_name = "число с плавающей точкой"

    test_true = [
        (None, 1.5),
        (None, 2.5),
        (None, 50.5),
        (None, 99.5),
        (None, 100.5),
        (None, 100.5),
    ]

    test_false = [
        (None, 1),
        (None, 2),
        (None, 50),
        (None, 99),
        (None, 100),

    ]

    test_exception = [
        (None, '100'),
        (None, 'a'),
        (None, (1, 2)),
        (None, [1, 2]),
        (None, {'a': 1}),
        (None, None),
        (None, True),
        (None, False),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, float):
            return True

        elif isinstance(value, int):
            return False

        elif isinstance(value, str):
            try:
                if value.isdigit() and '.' in value:
                    return True
            except ValueError:
                return False
        else:
            raise TypeError(f"Данные не являются числами: {type(value)}")


class IsNotFloat(Check):
    """Проверка на условие если значение не число с плавающей точкой"""
    verbose_name = "не число с плавающей точкой"

    test_true = [
        (None, 1),
        (None, 2),
        (None, 50),
        (None, '99'),
        (None, '100'),
    ]

    test_false = [
        (None, 1.5),
        (None, 2.5),
        (None, 50.5),
        (None, 99.5),
        (None, 100.5),

    ]

    test_exception = [
        (None, '100'),
        (None, 'a'),
        (None, (1, 2)),
        (None, [1, 2]),
        (None, {'a': 1}),
        (None, None),
        (None, True),
        (None, False),
    ]

    @staticmethod
    def check(_, value) -> bool:
        return not IsFloat.check(None, value)


class IsInt(Check):
    """Проверка на условие если значение целое число"""
    verbose_name = "целое число"

    test_true = [
        (None, 1),
        (None, 2),
        (None, 50),
        (None, '99'),
        (None, '100'),
    ]

    test_false = [
        (None, 1.5),
        (None, 2.5),
        (None, 50.5),
        (None, '99.5'),
        (None, '100.5'),
    ]

    test_exception = [
        (None, 'a'),
        (None, (1, 2)),
        (None, [1, 2]),
        (None, {'a': 1}),
        (None, None),
        (None, True),
        (None, False),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, int):
            return True

        elif isinstance(value, str):
            try:
                if value.isdigit() and '.' not in value:
                    return True
            except ValueError:
                return False
        elif isinstance(value, float):
            return False

        else:
            raise TypeError(f"Данные не являются числами: {type(value)}")


class IsNotInt(Check):
    """Проверка на условие если значение не целое число"""
    verbose_name = "не целое число"

    test_true = [
        (None, 1.5),
        (None, 2.5),
        (None, 50.5),
        (None, '99.5'),
        (None, '100.5'),
    ]

    test_false = [
        (None, 1),
        (None, 2),
        (None, 50),
        (None, '99'),
        (None, '100'),
    ]

    test_exception = [
        (None, 'a'),
        (None, (1, 2)),
        (None, [1, 2]),
        (None, {'a': 1}),
        (None, None),
        (None, True),
        (None, False),
    ]

    @staticmethod
    def check(_, value) -> bool:
        return not IsInt.check(None, value)


class Range(Check):
    """Проверка на условие если значение входит в диапазон"""
    verbose_name = "входит в диапазон"

    test_true = [
        (0.8, [0.1, 0.9]),
        (0.85, (0.81, 0.89)),
        (1.5, [1, 2]),
        (2.5, [1, 3]),
        (50.5, [1, 100]),
        (99, [1, 100]),
        (100, (1, 100)),
        (1, (1, 100)),
        (1000, (100, 10_000)),
        ]

    test_false = [
        (1, [0.5, 0.9]),
        (2, [2.5, 3]),
        (50, [51, 100]),
        (99, [1, 90]),
        (100, (1, 99)),
        (1, (2, 100)),
        (1000, (100, 999)),
        ]

    test_exception = [
        (None, 'a'),
        (None, (1, 2)),
        (None, [1, 2]),
        (None, {'a': 1}),
        (None, None),
        (None, True),
        (None, False),
        (1, (5, 2)),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(check_value, str) and check_value.isdigit():
            check_value = float(check_value)

        if isinstance(value, (list, tuple)):
            if len(value) != 2:
                raise ValueError(f"Диапазон должен состоять из двух значений: {check_value}")
            if value[0] > value[1]:
                raise ValueError(f"Начало диапазона ({value[0]}) должно быть меньше конца: {value[1]}")

            if value[0] <= check_value <= value[1]:
                return True

        else:
            raise TypeError(f"Данные не являются диапазоном: {type(check_value)}")

        return False


class NotRange(Check):
    """Проверка на условие если значение не входит в диапазон"""
    verbose_name = "не входит в диапазон"

    test_true = [
        (1, [0.5, 0.9]),
        (2, [2.5, 3]),
        (50, [51, 100]),
        (99, [1, 90]),
        (100, (1, 99)),
        (1, (2, 100)),
        (1000, (100, 999)),
        ]

    test_false = [
        (0.8, [0.1, 0.9]),
        (0.85, (0.81, 0.89)),
        (1.5, [1, 2]),
        (2.5, [1, 3]),
        (50.5, [1, 100]),
        (99, [1, 100]),
        (100, (1, 100)),
        (1, (1, 100)),
        (1000, (100, 10_000)),
        ]

    test_exception = [
        (None, 'a'),
        (None, (1, 2)),
        (None, [1, 2]),
        (None, {'a': 1}),
        (None, None),
        (None, True),
        (None, False),
        (1, (5, 2)),
        ]

    @staticmethod
    def check(check_value, value) -> bool:
        return not Range.check(check_value, value)
