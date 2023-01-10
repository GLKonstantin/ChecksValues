from check_module.check import Check


class IsBytes(Check):
    verbose_name = 'Проверка на тип bytes'

    test_true = [
        (None, b'123'),
        (None, b''),
        (None, b'1234567890'),
        (None, b'1234567890' * 100),
        (None, b' '),
    ]

    test_false = [
        (None, 123),
        (None, 123.456),
        (None, '123'),
        (None, '1234567890'),
        (None, '1234567890' * 100),
        (None, ' '),
        (None, True),
        (None, False),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, object()),
    ]

    @staticmethod
    def check(_, value):
        return isinstance(value, bytes)


class InBytes(Check):
    verbose_name = 'Проверка на нахождение в bytes'

    test_true = [
        (b'123', b'123'),
        (b'123', b'1234567890'),
        (b'123', b'1234567890' * 100),
        (b'123', b'555123555'),
        (b'123', b'1234567890' * 100 + b' '),
        (b'123', b' ' + b'1234567890' * 100),
        (b'123', b' ' + b'1234567890' * 100 + b' '),
        (b'123', b'1234567890' * 100 + b' ' + b'1234567890' * 100),
        (b'123', b' ' + b'1234567890' * 100 + b' ' + b'1234567890' * 100 + b' '),
    ]

    test_false = [
        (b'123', b'567'),
        (b'123', b'567890'),
        (b'123', b'567890' * 100),
        (b'123', b'555567555'),
        (b'123', b'567890' * 100 + b' '),
        (b'123', b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' '),
        (b'123', b'567890' * 100 + b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' ' + b'567890' * 100 + b' '),
    ]

    @staticmethod
    def check(search_value, value):
        if IsBytes.check(None, search_value) and IsBytes.check(None, value):
            return search_value in value
        else:
            return False


class NotInBytes(Check):
    verbose_name = 'Проверка на отсутствие в bytes'

    test_true = [
        (b'123', b'567'),
        (b'123', b'567890'),
        (b'123', b'567890' * 100),
        (b'123', b'555567555'),
        (b'123', b'567890' * 100 + b' '),
        (b'123', b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' '),
        (b'123', b'567890' * 100 + b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' ' + b'567890' * 100 + b' '),
    ]

    test_false = [
        (b'123', b'123'),
        (b'123', b'1234567890'),
        (b'123', b'1234567890' * 100),
        (b'123', b'555123555'),
        (b'123', b'1234567890' * 100 + b' '),
        (b'123', b' ' + b'1234567890' * 100),
        (b'123', b' ' + b'1234567890' * 100 + b' '),
        (b'123', b'1234567890' * 100 + b' ' + b'1234567890' * 100),
        (b'123', b' ' + b'1234567890' * 100 + b' ' + b'1234567890' * 100 + b' '),
    ]

    @staticmethod
    def check(search_value, value):
        if IsBytes.check(None, search_value) and IsBytes.check(None, value):
            return search_value not in value
        else:
            return False


class EqualBytes(Check):
    verbose_name = 'Проверка на равенство bytes'

    test_true = [
        (b'123', b'123'),
        (b'1234567890' * 100, b'1234567890' * 100),
        (b'1234567890' * 100 + b' ', b'1234567890' * 100 + b' '),
        (b' ' + b'1234567890' * 100, b' ' + b'1234567890' * 100),
        (b' ' + b'1234567890' * 100 + b' ', b' ' + b'1234567890' * 100 + b' '),
    ]

    test_false = [
        (b'123', b'567'),
        (b'123', b'567890'),
        (b'123', b'567890' * 100),
        (b'123', b'555567555'),
        (b'123', b'567890' * 100 + b' '),
        (b'123', b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' '),
        (b'123', b'567890' * 100 + b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' ' + b'567890' * 100 + b' '),
    ]

    @staticmethod
    def check(search_value, value):
        if IsBytes.check(None, search_value) and IsBytes.check(None, value):
            return search_value == value
        else:
            return False


class NotEqualBytes(Check):
    verbose_name = 'Проверка на неравенство bytes'

    test_true = [
        (b'123', b'567'),
        (b'123', b'567890'),
        (b'123', b'567890' * 100),
        (b'123', b'555567555'),
        (b'123', b'567890' * 100 + b' '),
        (b'123', b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' '),
        (b'123', b'567890' * 100 + b' ' + b'567890' * 100),
        (b'123', b' ' + b'567890' * 100 + b' ' + b'567890' * 100 + b' '),
    ]

    test_false = [
        (b'123', b'123'),
        (b'1234567890' * 100, b'1234567890' * 100),
        (b'1234567890' * 100 + b' ', b'1234567890' * 100 + b' '),
        (b' ' + b'1234567890' * 100, b' ' + b'1234567890' * 100),
        (b' ' + b'1234567890' * 100 + b' ', b' ' + b'1234567890' * 100 + b' '),
    ]

    @staticmethod
    def check(search_value, value):
        if IsBytes.check(None, search_value) and IsBytes.check(None, value):
            return search_value != value
        else:
            return False
