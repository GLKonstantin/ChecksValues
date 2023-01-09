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


if __name__ == '__main__':
    print(get_date_from_string('2020-91-01'))
    print(get_date_from_string('2020/01/71'))
    print(get_date_from_string('2020.01.02'))
    print(get_date_from_string('01-01-2020'))
    print(get_date_from_string('01.01.2020'))
    print(get_date_from_string('01/01/2020'))
    print('-----------------')
    print(get_time_from_string('01:01:20'))
    print(get_time_from_string('01:01:20.123456'))
    print(get_time_from_string('01:01:20.1234'))
    print(get_time_from_string('01:01:20.123456789'))
    print(get_time_from_string('01:01'))
    print(get_time_from_string('01.01.20.123456789'))

