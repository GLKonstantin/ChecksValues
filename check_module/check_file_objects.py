import os
from check_module.check import CheckConditions


class IsFile(CheckConditions):
    """Проверка на условие если значение является путем к файлу"""
    verbose_name = "является путем к существующему файлу"

    test_true = [
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check_base.py')),
    ]

    test_false = [
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py', 'check.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check.py', 'check_file_objects.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py', 'check.py', 'check_file_objects.py')),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return os.path.isfile(value)
        else:
            raise TypeError(f'Значение {value} не является строкой')


class IsDir(CheckConditions):
    """Проверка на условие если значение является путем к папке"""

    verbose_name = "является путем к  к существующей папке"

    test_true = [
        (None, os.path.dirname(__file__)),
        (None, os.path.dirname(os.path.dirname(__file__))),
        ]

    test_false = [
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check_base.py')),
        ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
        ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return os.path.isdir(value)
        else:
            raise TypeError(f'Значение {value} не является строкой')


class PathExists(CheckConditions):
    """Проверка на условие если папка существует"""

    verbose_name = "путь до файла или папки существует"

    test_true = [
        (None, os.path.dirname(__file__)),
        (None, os.path.dirname(os.path.dirname(__file__))),
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py')),
    ]

    test_false = [
        (None, os.path.join(os.path.dirname(__file__), 'fake_file.py')),
        (None, os.path.join(os.path.dirname(__file__), 'fake_file.txt')),
        (None, os.path.join(os.path.dirname(__file__), 'fake_file.jpg')),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return os.path.exists(value)
        else:
            raise TypeError(f'Значение {value} не является строкой')


class PathNotExists(CheckConditions):
    """Проверка на условие если папка не существует"""
    verbose_name = "папка не существует"

    test_true = [
        (None, os.path.join(os.path.dirname(__file__), 'fake_file.py')),
        (None, os.path.join(os.path.dirname(__file__), 'FAKE_DIR')),
        (None, os.path.join(os.path.dirname(__file__), 'FAKE_DIR', 'fake_file.jpg')),
    ]

    test_false = [
        (None, os.path.dirname(__file__)),
        (None, os.path.dirname(os.path.dirname(__file__))),
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py')),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            return not os.path.exists(value)
        else:
            raise TypeError(f'Значение {value} не является строкой')


class IsFileEmpty(CheckConditions):
    """Проверка на условие если файл пустой"""

    verbose_name = "файл пустой"

    test_true = [
        (None, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'empty_file_for_test.txt')),
    ]

    test_false = [
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check.py')),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            if os.path.isfile(value):
                return os.stat(value).st_size == 0
            else:
                raise TypeError(f'Путь {value} не является файлом')
        else:
            raise TypeError(f'Значение {value} не является строкой')


class IsDirEmpty(CheckConditions):
    """Проверка на условие если папка пустая"""
    verbose_name = "папка пустая"

    test_true = [
        (None, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'Empty_folder_for_test')),
    ]

    test_false = [
        (None, os.path.dirname(__file__)),
        (None, os.path.dirname(os.path.dirname(__file__))),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            if os.path.isdir(value):
                return len(os.listdir(value)) == 0
            else:
                raise TypeError(f'Путь {value} не является папкой')
        else:
            raise TypeError(f'Значение {value} не является путем (строкой)')


class IsFileNotEmpty(CheckConditions):
    """Проверка на условие если файл не пустой"""
    verbose_name = "файл не пустой"

    test_true = [
        (None, os.path.join(os.path.dirname(__file__), 'check_file_objects.py')),
        (None, os.path.join(os.path.dirname(__file__), 'check.py')),
    ]

    test_false = [
        (None, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'empty_file_for_test.txt')),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            if os.path.isfile(value):
                return os.stat(value).st_size != 0
            else:
                raise TypeError(f'Путь {value} не является файлом')
        else:
            raise TypeError(f'Значение {value} не является строкой')


class IsDirNotEmpty(CheckConditions):
    """Проверка на условие если папка не пустая"""
    verbose_name = "папка не пустая"

    test_true = [
        (None, os.path.dirname(__file__)),
        (None, os.path.dirname(os.path.dirname(__file__))),
    ]

    test_false = [
        (None, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'Empty_folder_for_test')),
    ]

    test_exception = [
        (None, None),
        (None, 1),
        (None, []),
        (None, {}),
        (None, ()),
        (None, set()),
        (None, True),
        (None, False),
        (None, 'string'),
    ]

    @staticmethod
    def check(_, value) -> bool:
        if isinstance(value, str):
            if os.path.isdir(value):
                return len(os.listdir(value)) != 0
            else:
                raise TypeError(f'Путь {value} не является папкой')
        else:
            raise TypeError(f'Значение {value} не является путем (строкой)')
