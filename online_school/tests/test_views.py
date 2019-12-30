#import pytest
# Create your tests here.
import unittest


class Tests(unittest.TestCase):
    def test_true(self):
        self.assertEqual(1, 1)