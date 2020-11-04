import unittest


def run_test():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests/', pattern='test_*.py')
    return test_suite
