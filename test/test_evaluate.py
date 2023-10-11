
import unittest
import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from main.input import *
from main.evaluate import *


class TestEvaluation(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()