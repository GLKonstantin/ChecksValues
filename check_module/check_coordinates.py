#  Copyright (c) by Konstantin Levickiy at 2023.
#

from check_module.check import CheckConditions


class IsCoordsValid(CheckConditions):
    """Проверка на условие если координаты валидны"""
    verbose_name = "координаты валидны"

    @staticmethod
    def check(check_value, value) -> bool:
        try:
            lat, lon = value.split(',')
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return False
        return -90 <= lat <= 90 and -180 <= lon <= 180


class IsCoordsInvalid(CheckConditions):
    """Проверка на условие если координаты не валидны"""
    verbose_name = "координаты не валидны"

    @staticmethod
    def check(check_value, value) -> bool:
        try:
            lat, lon = value.split(',')
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return True
        return not (-90 <= lat <= 90 and -180 <= lon <= 180)


class IsCoordsInRussia(CheckConditions):
    """Проверка на условие если координаты в России"""
    verbose_name = "координаты в России"

    @staticmethod
    def check(check_value, value) -> bool:
        try:
            lat, lon = value.split(',')
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return False
        return 41.2 <= lat <= 83.1 and 19.0 <= lon <= 190.0


class IsCoordsNotInRussia(CheckConditions):
    """Проверка на условие если координаты не в России"""
    verbose_name = "координаты не в России"

    @staticmethod
    def check(check_value, value) -> bool:
        try:
            lat, lon = value.split(',')
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return True
        return not (41.2 <= lat <= 83.1 and 19.0 <= lon <= 190.0)


class InBoxCoords(CheckConditions):
    """Проверка на условие если координаты внутри прямоугольника"""
    verbose_name = "координаты внутри прямоугольника"

    @staticmethod
    def check(check_value, value) -> bool:
        try:
            lat, lon = value.split(',')
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return False
        return check_value[0] <= lat <= check_value[1] and check_value[2] <= lon <= check_value[3]


class NotInBoxCoords(CheckConditions):
    """Проверка на условие если координаты не внутри прямоугольника"""
    verbose_name = "координаты не внутри прямоугольника"

    @staticmethod
    def check(check_value, value) -> bool:
        try:
            lat, lon = value.split(',')
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return True
        return not (check_value[0] <= lat <= check_value[1] and check_value[2] <= lon <= check_value[3])
