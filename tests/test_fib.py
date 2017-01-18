import unittest
from main.fib import fib_seq

class FibSeq(unittest.TestCase):
	def test_input_is_num(self):
		self.assertIsInstance(fib_seq(8), int)

if __name__ == '__main__':
	unittest.main()