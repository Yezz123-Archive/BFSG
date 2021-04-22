import string

from SG.BFSG import BruteForceStringGenerator, Direction

import unittest
import pytest


class MyTest(unittest.TestCase):
    def test_brute_force_empty(self):
        default_init = BruteForceStringGenerator()
        assert (next(default_init) == 'a')

    def test_brute_force_direction(self):
        direction_test = BruteForceStringGenerator(sequence='aa', direction=Direction.LEFT)
        assert (next(direction_test) == 'ba')
        direction_test = BruteForceStringGenerator(sequence='aa', direction=Direction.RIGHT)
        assert (next(direction_test) == 'ab')

    def test_brute_force_edge(self):
        direction_test = BruteForceStringGenerator(sequence='za', direction=Direction.LEFT)
        assert (next(direction_test) == 'ab')
        direction_test = BruteForceStringGenerator(sequence='az', direction=Direction.RIGHT)
        assert (next(direction_test) == 'ba')

    def test_brute_force_long_string(self):
        long_string = BruteForceStringGenerator(sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert (next(long_string) == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_brute_force_for_loop(self):
        loop_string = BruteForceStringGenerator(min_length=3)
        for _ in range(1, len(string.ascii_lowercase)):
            next(loop_string)
        assert (next(loop_string) == 'aaz')

        for _ in range(1, len(string.ascii_lowercase)):
            next(loop_string)
        assert (next(loop_string) == 'abz')

        for _ in range(1, len(string.ascii_lowercase * len(string.ascii_lowercase))):
            next(loop_string)
        assert (next(loop_string) == 'bbz')

    def test_brute_force_custom_chars(self):
        custom_string = BruteForceStringGenerator(chars='!@#', min_length=3)
        assert (next(custom_string) == '!!!')
        assert (next(custom_string) == '!!@')
        assert (next(custom_string) == '!!#')

    def test_brute_force_brute_left(self):
        brute_string = BruteForceStringGenerator(direction=Direction.LEFT)
        for _ in range(1, 2000000):
            next(brute_string)
        assert (next(brute_string) == 'botid')

    def test_brute_force_brute_right(self):
        brute_string = BruteForceStringGenerator()
        for _ in range(1, 2000000):
            next(brute_string)
        assert (next(brute_string) == 'ditob')

    def test_brute_force_max_length(self):
        with pytest.raises(StopIteration):
            brute_string = BruteForceStringGenerator('z', max_length=1)
            next(brute_string)

    def test_brute_force_generator(self):
        brute_string = BruteForceStringGenerator(max_length=3)
        for text in brute_string:
            pass
        assert (text == 'zzz')

    def test_not_direction_type(self):
        for i in range(-1, 2):
            with pytest.raises(ValueError):
                BruteForceStringGenerator('a', max_length=1, direction=i)

    def test_brute_force_with_space(self):
        custom_string = BruteForceStringGenerator(chars='a ', min_length=3)
        assert (next(custom_string) == 'aaa')
        assert (next(custom_string) == 'aa ')
        assert (next(custom_string) == 'a a')

    def test_brute_force_with_polish_letters(self):
        custom_string = BruteForceStringGenerator(chars='ąćęłńóśźż', min_length=3)
        for _ in range(1, 2003):
            next(custom_string)
        assert (next(custom_string) == 'ćśśń')

    def test_brute_force_with_polish_letters_backward(self):
        custom_string = BruteForceStringGenerator(chars='ąćęłńóśźż', min_length=3, direction=Direction.LEFT)
        for _ in range(1, 2003):
            next(custom_string)
        assert (next(custom_string) == 'ńśść')

    def test_brute_force_with_german_letters(self):
        custom_string = BruteForceStringGenerator(chars='äöüß', min_length=3)
        for _ in range(1, 2003):
            next(custom_string)
        assert (next(custom_string) == 'äüüöäü')

    def test_brute_force_with_german_letters_backward(self):
        custom_string = BruteForceStringGenerator(chars='äöüß', min_length=3, direction=Direction.LEFT)
        for _ in range(1, 2003):
            next(custom_string)
        assert (next(custom_string) == 'üäöüüä')

    def test_brute_force_with_czech_letters(self):
        custom_string = BruteForceStringGenerator(chars='ýžáčďéěíňóřšťúů', max_length=4)
        for _ in custom_string:
            pass
        assert (custom_string.sequence == 'ůůůý')

    def test_brute_force_with_czech_letters_backward(self):
        custom_string = BruteForceStringGenerator(chars='ýžáčďéěíňóřšťúů', max_length=4, direction=Direction.LEFT)
        for _ in custom_string:
            pass
        assert (custom_string.sequence == 'ýůůů')

    def test_brute_force_string_max_length(self):
        for i in range(1, 10):
            custom_string = BruteForceStringGenerator(chars='ab', max_length=i)
            for _ in custom_string:
                pass
            assert (len(custom_string) == i)
