import os
from .engine import Check


class IsPath(Check):
    """Проверка на условие если значение является путем к файлу или папке"""
    verbose_name = "является путем к файлу или папке"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) or os.path.isfile(value)


class IsFile(Check):
    """Проверка на условие если значение является путем к файлу"""
    verbose_name = "является путем к файлу"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value)


class IsDir(Check):
    """Проверка на условие если значение является путем к папке"""
    verbose_name = "является путем к папке"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value)


class IsFileExists(Check):
    """Проверка на условие если файл существует"""
    verbose_name = "файл существует"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value) and os.path.exists(value)


class IsDirExists(Check):
    """Проверка на условие если папка существует"""
    verbose_name = "папка существует"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) and os.path.exists(value)


class IsFileNotExists(Check):
    """Проверка на условие если файл не существует"""
    verbose_name = "файл не существует"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value) and not os.path.exists(value)


class IsDirNotExists(Check):
    """Проверка на условие если папка не существует"""
    verbose_name = "папка не существует"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) and not os.path.exists(value)


class IsFileEmpty(Check):
    """Проверка на условие если файл пустой"""
    verbose_name = "файл пустой"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value) and os.path.getsize(value) == 0


class IsDirEmpty(Check):
    """Проверка на условие если папка пустая"""
    verbose_name = "папка пустая"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) and not os.listdir(value)


class IsFileNotEmpty(Check):
    """Проверка на условие если файл не пустой"""
    verbose_name = "файл не пустой"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value) and os.path.getsize(value) > 0


class IsDirNotEmpty(Check):
    """Проверка на условие если папка не пустая"""
    verbose_name = "папка не пустая"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) and os.listdir(value)


class IsFileReadable(Check):
    """Проверка на условие если файл доступен для чтения"""
    verbose_name = "файл доступен для чтения"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value) and os.access(value, os.R_OK)


class IsDirReadable(Check):
    """Проверка на условие если папка доступна для чтения"""
    verbose_name = "папка доступна для чтения"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) and os.access(value, os.R_OK)


class IsFileWritable(Check):
    """Проверка на условие если файл доступен для записи"""
    verbose_name = "файл доступен для записи"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isfile(value) and os.access(value, os.W_OK)


class IsDirWritable(Check):
    """Проверка на условие если папка доступна для записи"""
    verbose_name = "папка доступна для записи"

    @staticmethod
    def check(check_value, value) -> bool:
        return os.path.isdir(value) and os.access(value, os.W_OK)