
class Check(object):
    """
    Базовый класс для спецификаций и проверки по значению
    """
    subclasses = {}
    tests = {}
    verbose_name = None
    CHOOSE = []

    def is_satisfied_by(self, check_name, check_value, value) -> bool:
        """
        Проверка по значению

        :param check_name: имя класса проверки, например, 'Equal' или класс проверки, например, Equal
        или первое значение из кортежа CHOOSE

        :param check_value: значение для проверки
        :param value: значение для проверки
        :return: bool
        """

        if isinstance(check_name, str):
            check_class = self.subclasses.get(check_name)
        else:
            check_class = self.subclasses.get(check_name.__name__)

        if check_class:
            return check_class.check(check_value, value=value)

        print(f'Неизвестное условие {check_name}')
        return False

    def __str__(self):
        return 'Checks'

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def __init_subclass__(cls, **kwargs):
        """ Регистрация классов проверок """
        super().__init_subclass__(**kwargs)
        # Устанавливаем атрибут класса Check в соответствии с именем класса проверки для доступа к классу проверки
        # Например, class Equal можно получить через Check.Equal
        setattr(Check, cls.__name__, cls.__name__)
        # Заполняем verbose_name для отображения в интерфейсе при выборе проверки
        if hasattr(cls, 'verbose_name'):
            cls.CHOOSE.append((cls.__name__, cls.verbose_name))
        else:
            cls.CHOOSE.append((cls.__name__, cls.__name__))

        # Создаем словарь для проведения тестов
        Check.tests[cls.__name__] = {}
        if hasattr(cls, 'test_true'):
            Check.tests[cls.__name__]['True'] = cls.test_true
        if hasattr(cls, 'test_false'):
            Check.tests[cls.__name__]['False'] = cls.test_false
        if hasattr(cls, 'test_exception'):
            Check.tests[cls.__name__]['Exception'] = cls.test_exception

        # Если Check.tests[cls_name] пустой, то удаляем его
        if not Check.tests[cls.__name__]:
            Check.tests.pop(cls.__name__)

        # Регистрируем класс проверки в словаре подклассов
        Check.subclasses[cls.__name__] = cls
