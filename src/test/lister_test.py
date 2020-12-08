# Created by Leon Hunter at 11:23 AM 10/24/2020
from numbers import Number
from unittest import TestCase

from src.main.lister import Lister


class ListerTest(TestCase):
    def _test(self, method_to_test, value_sets):
        for value_set in value_sets:
            # given
            function_tested = method_to_test.__name__

            first_value = value_set[0]
            second_value = value_set[1]
            third_value = value_set[2]
            expected_calculation = value_set[3]

            # when
            actual_calculation = method_to_test(first_value, second_value, third_value)

            calculation_error_message = '''
            function_tested = {}
            first_value = {}
            second_value = {}
            third_value = {}
            expected_calculation = {}
            actual_calculation = {}
            '''.format(function_tested, first_value, second_value, third_value, expected_calculation,
                       actual_calculation)

            # then
            self.assertEquals(expected_calculation, actual_calculation, calculation_error_message)

    def test_get_integer_list(self):
        self._test(Lister().get_integer_list, [
            (0, 0, 0, [0]),
            (0, 10, 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            (0, 10, 2, [0, 2, 4, 6, 8, 10]),
            (0, 10, 3, [0, 3, 6, 9]),
            (0, 10, 5, [0, 5, 10]),
            (1, 15, 2, [1, 3, 5, 7, 9, 11, 13, 15]),
            (1, 15, 3, [1, 4, 7, 10, 13])
        ])

    def test_get_even_list(self):
        self._test(Lister().get_even_list, [
            (0, 0, 0, [0]),
            (0, 10, 1, [0, 2, 4, 6, 8, 10]),
            (0, 10, 2, [0, 2, 4, 6, 8, 10]),
            (0, 10, 3, [0, 6]),
            (0, 10, 5, [0, 10]),
            (1, 15, 2, []),
            (1, 15, 3, [4, 10])
        ])

    def test_get_odd_list(self):
        self._test(Lister().get_odd_list, [
            (0, 0, 0, []),
            (0, 10, 1, [1, 3, 5, 7, 9]),
            (0, 10, 2, []),
            (0, 10, 3, [3, 9]),
            (0, 10, 5, [5]),
            (1, 15, 2, [1, 3, 5, 7, 9, 11, 13, 15]),
            (1, 15, 3, [1, 7, 13])
        ])
