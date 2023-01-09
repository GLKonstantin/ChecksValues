from check_module.engine import Check
from check_module.check_utils import get_list_from_string


class Equal(Check):
    """Проверка равенства значений"""
    verbose_name = "равно"
    test_true = [
        ('TestTrue', 'TestTrue'),
        ('TestFalse', 'TestFalse'),
        (100, 100),
        (100.0, 100.0),
        (100.0, 100),
        ([1, 2, 3], [1, 2, 3]),
        ((1, 2, 3), (1, 2, 3)),
        ({'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
    ]
    test_false = [
        ('TestFalse', 'TestTrue'),
        ('TestTrue', 'TestFalse'),
        (100, 200),
        (100.0, 200),
        (100.0, 200.0),
        ([1, 2, 3], [1, 2, 3, 4]),
        ((1, 2, 3), (1, 2, 3, 4)),
        ({'a': 1, 'b': 2}, {'a': 1, 'b': 3}),
    ]
    test_exception = [
        ('TestException', 100),
        (100, 'TestException'),

    ]

    @staticmethod
    def check(check_value, value) -> bool:
        """Проверка условия"""
        return value == check_value


class NotEqual(Check):
    """Проверка неравенства значений"""
    verbose_name = "не равно"
    test_true = [
        ('TestTrue', 'TestFalse'),
        (100, 200),
        (100.0, 200),
        (100.0, 200.0),
        ([1, 2, 3], [1, 2, 3, 4]),
        ((1, 2, 3), (1, 2, 3, 4)),
        ({'a': 1, 'b': 2}, {'a': 1, 'b': 3}),
    ]
    test_false = [
        ('TestFalse', 'TestFalse'),
        ('TestTrue', 'TestTrue'),
        (100, 100),
        (100.0, 100.0),
        (100.0, 100),
        ([1, 2, 3], [1, 2, 3]),
        ((1, 2, 3), (1, 2, 3)),
        ({'a': 1, 'b': 2}, {'a': 1, 'b': 2}),

    ]
    test_exception = [
        ('TestException', 100),
        (100, 'TestException'),

    ]

    @staticmethod
    def check(check_value, value) -> bool:
        return value != check_value


class In(Check):
    """Проверка на условие если значение в списке"""
    verbose_name = "в списке"

    test_true = [
        (100, [100, 200]),
        ('TestTrue', ('TestTrue', 'TestFalse')),
        ('TestFalse', ('TestTrue', 'TestFalse')),
        ('TestTrue', ['TestTrue', 'TestTrue']),
        ('TestTrue', 'TestTrue TestFalse'),
        ('TestTrue', 'TestTrue,TestFalse'),
        ('TestTrue', 'TestTrue, TestFalse'),
        ('TestTrue', 'TestTrue;TestFalse;TestTrue'),
        ('TestTrue', 'TestTrue; TestFalse; TestTrue'),
    ]

    test_false = [
        (100, [200, 200]),
        ('TestFalse', ('TestTrue', 'TestTrue')),
        ('TestTrue', ('TestFalse', 'TestFalse')),
        ('TestTrue', 'TestFalse TestFalse'),
        ('TestTrue', ['TestFalse', 'TestNone']),
        ('TestTrue', 'TestNone TestNone'),
        ('TestTrue', 'TestNone,TestNone'),
        ('TestTrue', 'TestNone, TestNone'),
        ('TestTrue', 'TestNone;TestNone;TestNone'),
        ('TestTrue', 'TestNone; TestNone; TestNone'),
    ]

    test_exception = [
        ('TestException', ('TestException', 100)),
        ('TestException', ['TestException', 100]),
        ('TestException', 100),
    ]

    @staticmethod
    def check(check_value, value) -> bool:

        if isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set) or isinstance(value, dict):
            return check_value in value

        elif isinstance(value, str):
            return check_value in get_list_from_string(value)

        return value in check_value


class NotIn(Check):
    """Проверка на условие если значение не в списке"""
    verbose_name = "не в списке"

    test_true = [
        (100, [200, 200]),
        ('TestFalse', ('TestTrue', 'TestTrue')),
        ('TestTrue', ('TestFalse', 'TestFalse')),
        ('TestTrue', 'TestFalse TestFalse'),
        ('TestTrue', ['TestFalse', 'TestNone']),
        ('TestTrue', 'TestNone TestNone'),
        ('TestTrue', 'TestNone,TestNone'),
        ('TestTrue', 'TestNone, TestNone'),
        ('TestTrue', 'TestNone;TestNone;TestNone'),
        ('TestTrue', 'TestNone; TestNone; TestNone'),
    ]

    test_false = [
        (100, [100, 200]),
        ('TestTrue', ('TestTrue', 'TestFalse')),
        ('TestFalse', ('TestTrue', 'TestFalse')),
        ('TestTrue', ['TestTrue', 'TestTrue']),
        ('TestTrue', 'TestTrue TestFalse'),
        ('TestTrue', 'TestTrue,TestFalse'),
        ('TestTrue', 'TestTrue, TestFalse'),
        ('TestTrue', 'TestTrue;TestFalse;TestTrue'),
        ('TestTrue', 'TestTrue; TestFalse; TestTrue'),
    ]

    test_exception = [
        ('TestException', ('TestException', 100)),
        ('TestException', ['TestException', 100]),
        ('TestException', 100),
    ]

    @staticmethod
    def check(check_value, value) -> bool:
        if isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set) or isinstance(value, dict):
            return check_value not in value

        elif isinstance(value, str):
            return check_value not in get_list_from_string(value)
        return check_value not in value


class IsTrue(Check):
    """Проверка на условие если значение True"""
    verbose_name = "истина"

    test_true = [
        ('None', True),
        ('None', 1),
        ('None', 1.0),
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    test_false = [
        ('None', False),
        (None, 0),
        (None, 0.0),
        (None, ''),
        (None, []),
        (None, ()),
        (None, {}),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, bool):
            return value is True
        return bool(value)


class IsFalse(Check):
    """Проверка на условие если значение False"""
    verbose_name = "ложь"

    test_true = [
        ('None', False),
        (None, 0),
        (None, 0.0),
        (None, ''),
        (None, []),
        (None, ()),
        (None, {}),
    ]

    test_false = [
        ('None', True),
        ('None', 1),
        ('None', 1.0),
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, bool):
            return value is False
        return not bool(value)


class IsEmpty(Check):
    """Проверка на условие если значение пустое"""
    verbose_name = "пустая строка"

    test_true = [
        ('None', ''),
        ('None', []),
        ('None', ()),
        ('None', {}),
    ]

    test_false = [
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    test_exception = [
        ('None', True),
        ('None', 1),
        ('None', 1.0),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return value == ''
        elif isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set) or isinstance(value, dict):
            return len(value) == 0


class IsNotEmpty(Check):
    """Проверка на условие если значение не пустое"""
    verbose_name = "не пустая строка"

    test_true = [
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    test_false = [
        ('None', ''),
        ('None', []),
        ('None', ()),
        ('None', {}),
    ]

    test_exception = [
        ('None', True),
        ('None', 1),
        ('None', 1.0),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return value != ''
        elif isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set) or isinstance(value, dict):
            return len(value) != 0


class IsNone(Check):
    """Проверка на условие если значение None"""
    verbose_name = "не определено"

    test_true = [
        ('None', None),
    ]

    test_false = [
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    @staticmethod
    def check(_, value) -> bool:
        return value is None


class IsNotNone(Check):
    """Проверка на условие если значение не None"""
    verbose_name = "не пустое"

    test_true = [
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    test_false = [
        ('None', None),
    ]

    @staticmethod
    def check(_, value) -> bool:
        return value is not None


class IsDigit(Check):
    """Проверка на условие если значение цифра"""
    verbose_name = "цифра"

    test_true = [
        ('None', 1),
        ('None', 1.0),
    ]

    test_false = [
        ('None', 'TestTrue'),
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    test_exception = [
        ('None', True),
        ('None', None),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, int) or isinstance(value, float):
            return True
        elif isinstance(value, str):
            return value.isdigit()
        return False


class IsAlphaOrDigit(Check):
    """Проверка на условие если значение буква или цифра"""
    verbose_name = "буква или цифра"

    test_true = [
        ('None', 'TestTrue'),
        ('None', 1),
        ('None', 1.0),
    ]

    test_false = [
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
    ]

    test_exception = [
        ('None', True),
        ('None', None),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return value.isalnum()
        elif isinstance(value, int) or isinstance(value, float):
            return True
        return False


class IsAlpha(Check):
    """Проверка на условие если значение буква"""
    verbose_name = "буква"

    test_true = [
        ('None', 'TestTrue'),
    ]

    test_false = [
        ('None', ['TestTrue']),
        ('None', ('TestTrue',)),
        ('None', {'TestTrue': 1}),
        ('None', 1),
        ('None', 1.0),

    ]

    test_exception = [
        ('None', True),
        ('None', None),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return value.isalpha()
        return False
