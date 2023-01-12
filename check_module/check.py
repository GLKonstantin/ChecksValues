
class CheckConditions(object):
    """
    Базовый класс для спецификаций и проверки по значению
    """
    subclasses = {}
    tests = {}
    verbose_name = None
    CHOOSE = []

    @classmethod
    def is_satisfied_by(cls, check_name, check_value, value) -> bool:
        """
        Проверка по значению

        :param check_name: имя класса проверки, например, 'Equal' или класс проверки, например, Equal
        или первое значение из кортежа CHOOSE

        :param check_value: значение для проверки
        :param value: значение для проверки
        :return: bool
        """

        if isinstance(check_name, str):
            check_class = cls.subclasses.get(check_name)
        else:
            check_class = cls.subclasses.get(check_name.__name__)

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
        setattr(CheckConditions, cls.__name__, cls.__name__)
        # Заполняем verbose_name для отображения в интерфейсе при выборе проверки
        if hasattr(cls, 'verbose_name'):
            cls.CHOOSE.append((cls.__name__, cls.verbose_name))
        else:
            cls.CHOOSE.append((cls.__name__, cls.__name__))

        # Создаем словарь для проведения тестов
        CheckConditions.tests[cls.__name__] = {}
        if hasattr(cls, 'test_true'):
            CheckConditions.tests[cls.__name__]['True'] = cls.test_true
        if hasattr(cls, 'test_false'):
            CheckConditions.tests[cls.__name__]['False'] = cls.test_false
        if hasattr(cls, 'test_exception'):
            CheckConditions.tests[cls.__name__]['Exception'] = cls.test_exception

        # Если Check.tests[cls_name] пустой, то удаляем его
        if not CheckConditions.tests[cls.__name__]:
            CheckConditions.tests.pop(cls.__name__)

        # Регистрируем класс проверки в словаре подклассов
        CheckConditions.subclasses[cls.__name__] = cls


class CheckActions:
    """Проверка действий события (Создание, изменение и удаление записи)"""
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'
    CREATE_OR_UPDATE = (CREATE, UPDATE)
    CREATE_OR_DELETE = (CREATE, DELETE)
    UPDATE_OR_DELETE = (UPDATE, DELETE)
    ALL = (CREATE, UPDATE, DELETE)

    CHOOSE = (
        (CREATE, 'Создание'),
        (UPDATE, 'Изменение'),
        (DELETE, 'Удаление'),
        (CREATE_OR_UPDATE, 'Создание или изменение'),
        (CREATE_OR_DELETE, 'Создание или удаление'),
        (UPDATE_OR_DELETE, 'Изменение или удаление'),
        (ALL, 'Все'),
    )

    test_true = (
        (CREATE, 'create'),
        (UPDATE, 'update'),
        (DELETE, 'delete'),
        (CREATE_OR_UPDATE, 'create'),
        (CREATE_OR_UPDATE, 'update'),
        (CREATE_OR_DELETE, 'create'),
        (CREATE_OR_DELETE, 'delete'),
        (UPDATE_OR_DELETE, 'update'),
        (UPDATE_OR_DELETE, 'delete'),
        (ALL, 'create'),
        (ALL, 'update'),
        (ALL, 'delete'),
    )

    test_false = (
        (CREATE, 'update'),
        (CREATE, 'delete'),
        (UPDATE, 'create'),
        (UPDATE, 'delete'),
        (DELETE, 'create'),
        (DELETE, 'update'),
        (CREATE_OR_UPDATE, 'delete'),
        (CREATE_OR_DELETE, 'update'),
        (UPDATE_OR_DELETE, 'create'),
        (ALL, 'update'),
        (ALL, 'delete'),
    )

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return 'CheckActions'

    def __repr__(self):
        return f'{self.__class__.__name__}'

    @staticmethod
    def is_satisfied_by(check_action, create_flag):
        """
        Проверка действия события
        :param check_action: действие события из CHOOSE
        :param create_flag: флаг создания записи, True - создание, False - изменение, None - удаление
        :return: bool
        """

        def check(action, flag):
            if action == CheckActions.CREATE:
                if flag:
                    return True
            elif action == CheckActions.UPDATE:
                if flag is False:
                    return True
            elif action == CheckActions.DELETE:
                if flag is None:
                    return True
            elif action == CheckActions.CREATE_OR_UPDATE:
                if flag is not None:
                    return True
            elif action == CheckActions.CREATE_OR_DELETE:
                if flag is not None or flag is False:
                    return True
            elif action == CheckActions.UPDATE_OR_DELETE:
                if flag is False or flag is None:
                    return True
            elif action == CheckActions.ALL:
                return True

            return False

        if isinstance(check_action, (tuple, list)):
            return any(check(action, create_flag) for action in check_action)
        else:
            return check(check_action, create_flag)