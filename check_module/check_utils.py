import re
import datetime


def get_list_from_string(value):
    """Преобразование строки в список"""
    if isinstance(value, str):
        value = value.replace(',', ' ')
        value = value.replace(';', ' ')
        value = [v for v in value.split(' ') if v]
        return value
    else:
        return value


def get_date_from_string(value):
    """Преобразование строки в дату"""

    if isinstance(value, datetime.date):
        return value

    # Шаблоны дат для проверки по регулярному выражению с проверкой значений дней и месяцев
    templates = {
        'YYYY-MM-DD': r'^(?P<year>\d{4})[-\/.](?P<month>\d{2})[-\/.](?P<day>\d{2})',
        'DD-MM-YYYY': r'^(?P<day>\d{2})[-\/.](?P<month>\d{2})[-\/.](?P<year>\d{4})',
        'DD-MM-YY': r'^(?P<day>\d{2})[-\/.](?P<month>\d{2})[-\/.](?P<year>\d{2})',
        'YY-MM-DD': r'^(?P<year>\d{2})[-\/.](?P<month>\d{2})[-\/.](?P<day>\d{2})',
    }
    # Проверка на соответствие шаблону
    if isinstance(value, str):
        for template in templates.values():
            match_val = re.match(template, value)

            if match_val:
                match_val = match_val.groupdict()

                year = match_val.get('year')
                month = match_val.get('month')
                day = match_val.get('day')

                if year:
                    year = int(year)
                    if year < 100:
                        year += 2000
                    elif year > datetime.datetime.now().year:
                        return None

                if month:
                    month = int(month)
                    if month > 12:
                        return None

                if day:
                    day = int(day)
                    if day > 31:
                        return None
                return datetime.datetime(year, month, day)
    else:
        return None


def get_time_from_string(value):
    """Преобразование строки в формат времени datetime"""

    if isinstance(value, datetime.time):
        return value

    elif isinstance(value, datetime.datetime):
        return value.time()

    # Шаблоны времени для проверки по регулярному выражению с проверкой значений часов, минут, секунд и микросекунд
    templates = {
        'HH:MM:SS.MS': r'^(?P<hour>\d{2})[:.-](?P<minute>\d{2})[:.-](?P<second>\d{2})[:.](?P<microsecond>\d{4,6})$',
        'HH:MM:SS': r'^(?P<hour>\d{2})[:.-](?P<minute>\d{2})[:.-](?P<second>\d{2})$',
        'HH:MM': r'^(?P<hour>\d{2})[:.-](?P<minute>\d{2})$',
    }

    # Проверка на соответствие шаблону
    if isinstance(value, str):
        for template in templates.values():
            match_val = re.match(template, value)
            if match_val:
                match_val = match_val.groupdict()

                hour = match_val.get('hour')
                minute = match_val.get('minute')
                second = match_val.get('second')
                microsecond = match_val.get('microsecond')

                if hour:
                    hour = int(hour)
                    if hour > 23:
                        return None

                if minute:
                    minute = int(minute)
                    if minute > 59:
                        return None

                if second:
                    second = int(second)
                    if second > 59:
                        return None

                if microsecond:
                    microsecond = int(microsecond)

                return datetime.time(
                    # day=1,
                    # month=1,
                    # year=1,
                    hour=hour,
                    minute=minute,
                    second=second or 0,
                    microsecond=microsecond or 0,
                )

    return None


def get_datetime_from_string(value):
    """Преобразование строки в формат даты и времени datetime"""
    # Шаблоны даты и времени для проверки по регулярному выражению с
    # проверкой значений дней, месяцев, часов, минут, секунд и микросекунд
    templates = {
        'YYYY-MM-DD HH:MM:SS.MS':
            r'^(?P<year>\d{4})[-\/.](?P<month>\d{2})[-\/.](?P<day>\d{2})\s(?P<hour>\d{2})[:.-]'
            r'(?P<minute>\d{2})[:.-](?P<second>\d{2})[:.](?P<microsecond>\d{4,6})$',
        'YYYY-MM-DD HH:MM:SS': r'^(?P<year>\d{4})[-\/.](?P<month>\d{2})[-\/.]'
                               r'(?P<day>\d{2})\s(?P<hour>\d{2})[:.-](?P<minute>\d{2})[:.-](?P<second>\d{2})$',
        'YYYY-MM-DD HH:MM': r'^(?P<year>\d{4})[-\/.](?P<month>\d{2})[-\/.]'
                            r'(?P<day>\d{2})\s(?P<hour>\d{2})[:.-](?P<minute>\d{2})$',
        'DD-MM-YYYY HH:MM:SS.MS': r'^(?P<day>\d{2})[-\/.](?P<month>\d{2})[-\/.](?P<year>\d{4})\s(?P<hour>\d{2})[:.-]'
                                  r'(?P<minute>\d{2})[:.-](?P<second>\d{2})[:.](?P<microsecond>\d{4,6})$',
        'DD-MM-YYYY HH:MM:SS': r'^(?P<day>\d{2})[-\/.](?P<month>\d{2})[-\/.](?P<year>\d{4})\s(?P<hour>\d{2})[:.-]'
                               r'(?P<minute>\d{2})[:.-](?P<second>\d{2})$',
        'DD-MM-YYYY HH:MM': r'^(?P<day>\d{2})[-\/.](?P<month>\d{2})[-\/.](?P<year>\d{4})\s(?P<hour>\d{2})[:.-]'
                            r'(?P<minute>\d{2})$',
    }

    # Проверка на соответствие шаблону
    if isinstance(value, str):
        for template in templates.values():
            match_val = re.match(template, value)
            if match_val:
                match_val = match_val.groupdict()

                year = match_val.get('year')
                month = match_val.get('month')
                day = match_val.get('day')
                hour = match_val.get('hour')
                minute = match_val.get('minute')
                second = match_val.get('second')
                microsecond = match_val.get('microsecond')

                if year:
                    year = int(year)
                    if year > 9999:
                        return None

                if month:
                    month = int(month)
                    if month > 12:
                        return None

                if day:
                    day = int(day)
                    if day > 31:
                        return None

                if hour:
                    hour = int(hour)
                    if hour > 23:
                        return None

                if minute:
                    minute = int(minute)
                    if minute > 59:
                        return None

                if second:
                    second = int(second)
                    if second > 59:
                        return None

                if microsecond:
                    microsecond = int(microsecond)

                return datetime.datetime(
                    day=day,
                    month=month,
                    year=year,
                    hour=hour or 0,
                    minute=minute or 0,
                    second=second or 0,
                    microsecond=microsecond or 0,
                )

    return None


MONTHS = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12,
    # со склонениями
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12,
    # ----------------
    'янв': 1,
    'фев': 2,
    'мар': 3,
    'апр': 4,
    'июн': 6,
    'июл': 7,
    'авг': 8,
    'сен': 9,
    'окт': 10,
    'ноя': 11,
    'дек': 12,
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12,
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12,
}

WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6,
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
    'mon': 0,
    'tue': 1,
    'wed': 2,
    'thu': 3,
    'fri': 4,
    'sat': 5,
    'sun': 6,
    'пн': 0,
    'вт': 1,
    'ср': 2,
    'чт': 3,
    'пт': 4,
    'сб': 5,
    'вс': 6,
}


if __name__ == '__main__':
    pass
