#  Copyright (c) by Konstantin Levickiy at 2023.
#
import pytest

import check_module
from unittest import TestCase
from parameterized import parameterized


def collect_test_data():
    check = check_module.engine.Check()
    tests = check.tests
    run_tests = []
    for test in tests:
        func = check_module.engine.Check.subclasses.get(test)
        test_data_attrs = [attr for attr in dir(func) if attr.startswith('test_')]
        test_true_data = func.test_true if 'test_true' in test_data_attrs else None
        test_false_data = func.test_false if 'test_false' in test_data_attrs else None
        test_exception_data = func.test_exception if 'test_exception' in test_data_attrs else None
        if test_true_data:
            for i, data in enumerate(test_true_data):
                test_name = func.__name__+'_True_'+str(i+1)
                run_tests.append((test_name, check.is_satisfied_by, func, data, True))

        if test_false_data:
            for i, data in enumerate(test_false_data):
                test_name = func.__name__+'_False_'+str(i+1)
                run_tests.append((test_name, check.is_satisfied_by, func, data, False))

        if test_exception_data:
            for i, data in enumerate(test_exception_data):
                test_name = func.__name__+'_Exception_'+str(i+1)
                run_tests.append((test_name, check.is_satisfied_by, func, data, Exception))
    print(run_tests)
    return run_tests


class GenerateTest(TestCase):

    @parameterized.expand(collect_test_data())
    def test(self, name, main_func, func, data, expected):

        if expected == Exception:
            self.assertRaises(Exception, main_func, (func, *data))
        elif expected:
            res = main_func(func, *data)
            self.assertTrue(res, f'{func.__name__} - {data} - {res}')
        elif not expected:
            res = main_func(func, *data)
            self.assertFalse(res, f'{func.__name__} - {data} - {res}')
        else:
            raise Exception('Wrong expected value')


if __name__ == '__main__':
    print(*collect_test_data(), sep='\n')
