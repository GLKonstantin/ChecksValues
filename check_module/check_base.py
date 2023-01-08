from check_module.engine import Check


class Equal(Check):
    """Проверка равенства значений"""
    verbose_name = "равно"
    test_true = [('TestTrue', 'TestTrue'), ('TestFalse', 'TestFalse')]
    test_false = [('TestFalse', 'TestTrue'), ('TestTrue', 'TestFalse')]
    test_exception = [('TestException', 100)]

    @staticmethod
    def check(check_value, value) -> bool:
        """Проверка условия"""
        return value == check_value


class NotEqual(Check):
    """Проверка неравенства значений"""
    verbose_name = "не равно"
    test_true = [('TestTrue', 'TestFalse')]
    test_false = [('TestFalse', 'TestFalse')]
    test_exception = [('TestException', 100)]

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
            if ' ' in value and ',' not in value and ';' not in value:
                return check_value in value.split(' ')
            elif ',' in value:
                return check_value in value.split(',')
            elif ';' in value:
                return check_value in value.split(';')
            else:
                return check_value in value.split()
        return value in check_value


class NotIn(Check):
    """Проверка на условие если значение не в списке"""
    verbose_name = "не в списке"

    @staticmethod
    def check(check_value, value) -> bool:
        return value not in check_value


class IsTrue(Check):
    """Проверка на условие если значение True"""
    verbose_name = "истина"

    @staticmethod
    def check(check_value, value) -> bool:
        return value is True


class IsFalse(Check):
    """Проверка на условие если значение False"""
    verbose_name = "ложь"

    @staticmethod
    def check(check_value, value) -> bool:
        return value is False


class IsEmpty(Check):
    """Проверка на условие если значение пустое"""
    verbose_name = "пустая строка"

    @staticmethod
    def check(check_value, value) -> bool:
        return value == ''


class IsNotEmpty(Check):
    """Проверка на условие если значение не пустое"""
    verbose_name = "не пустая строка"

    @staticmethod
    def check(check_value, value) -> bool:
        return value != ''


class IsNone(Check):
    """Проверка на условие если значение None"""
    verbose_name = "не определено"

    @staticmethod
    def check(check_value, value) -> bool:
        return value is None


class IsNotNone(Check):
    """Проверка на условие если значение не None"""
    verbose_name = "не пустое"

    @staticmethod
    def check(check_value, value) -> bool:
        return value is not None


class IsDigit(Check):
    """Проверка на условие если значение цифра"""
    verbose_name = "цифра"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.isdigit()


class IsAlphaOrDigit(Check):
    """Проверка на условие если значение буква или цифра"""
    verbose_name = "буква или цифра"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.isalnum()


class IsAlpha(Check):
    """Проверка на условие если значение буква"""
    verbose_name = "буква"

    @staticmethod
    def check(check_value, value) -> bool:
        return value.isalpha()


class IsIn(Check):
    """Проверка на условие если значение входит в список"""
    verbose_name = "входит в список"

    @staticmethod
    def check(check_value, value) -> bool:
        return value in check_value


class IsNotIn(Check):
    """Проверка на условие если значение не входит в список"""
    verbose_name = "не входит в список"

    @staticmethod
    def check(check_value, value) -> bool:
        return value not in check_value
