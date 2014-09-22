__author__ = 'xxdpavelxx'
import unittest
from kafka_stream import runner
class Test(unittest.TestCase):
    def test_no_errors(self):
        self.assertTrue(runner,1)
if __name__ == "__main__":
    unittest.main()