# Created by Leon Hunter at 11:23 AM 10/24/2020
from unittest import TestCase

from src.main.filterer import Filterer


class FitlererTest(TestCase):
    def _test_binary_function(self, method_to_test, value_sets):
        for value_set in value_sets:
            # given
            function_tested = method_to_test.__name__

            first_value = value_set[0]
            second_value = value_set[1]
            expected_calculation = value_set[2]

            # when
            actual_calculation = method_to_test(first_value, second_value)

            calculation_error_message = '''
            function_tested = {}
            first_value = {}
            second_value = {}
            expected_calculation = {}
            actual_calculation = {}
            '''.format(function_tested, first_value, second_value, expected_calculation,
                       actual_calculation)

            # then
            self.assertEquals(expected_calculation, actual_calculation, msg=calculation_error_message)

    def _test_unary_function(self, method_to_test, value_sets):
        for value_set in value_sets:
            # given
            function_tested = method_to_test.__name__

            first_value = value_set[0]
            expected_calculation = value_set[1]

            # when
            actual_calculation = method_to_test(first_value)

            calculation_error_message = '''
            function_tested = {}
            first_value = {}
            expected_calculation = {}
            actual_calculation = {}
            '''.format(function_tested, first_value, expected_calculation,
                       actual_calculation)

            # then
            self.assertEqual(expected_calculation, actual_calculation, msg=calculation_error_message)

    def test_remove_characters(self):
        self._test_binary_function(Filterer().remove_characters, [
            (  # test case 0
                "Hello!",
                "He!",
                "llo"),

            (  # test case 1
                "Hello!",
                "!",
                "Hello"),

            (  # test case 2
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "a",
                ""),

            (  # test case 3
                "the quick brown fox jumps over the lazy dog",
                "abcdefghijklmnopqrstuvwxyz ",
                ""),

            (  # test case 4
                "The Quick Brown Fox Jumps Over The Lazy Dog",
                "the quick brown fox jumps over the lazy dog",
                "TQBFJOTLD"),

            (  # test case 5
                "the quick brown fox jumps over the lazy dog",
                "The Quick Brown Fox Jumps Over The Lazy Dog",
                "tqbfjtld")
        ])

    def test_remove_vowels(self):
        self._test_unary_function(Filterer().remove_vowels, [
            (  # test case 0
                "Hello!",
                "Hll!"),

            (  # test case 1
                "Hey!",
                "Hy!"),

            (  # test case 2
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                ""),

            (  # test case 3
                "the quick brown fox jumps over the lazy dog",
                "th qck brwn fx jmps vr th lzy dg"),

            (  # test case 4
                "The Quick Brown Fox Jumps Over The Lazy Dog",
                "Th Qck Brwn Fx Jmps vr Th Lzy Dg"),

            (  # test case 5
                "aeiou",
                "")
        ])

    def test_remove_consonants(self):
        self._test_unary_function(Filterer().remove_consonants, [
            (  # test case 0
                "Hello!",
                "eo!"),

            (  # test case 1
                "Hey!",
                "e!"),

            (  # test case 2
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),

            (  # test case 3
                "the quick brown fox jumps over the lazy dog",
                "e ui o o u oe e a o"),

            (  # test case 4
                "The Quick Brown Fox Jumps Over The Lazy Dog",
                "e ui o o u Oe e a o"),

            (  # test case 5
                "The quickest of brown foxes",
                "e uie o o oe")
        ])
