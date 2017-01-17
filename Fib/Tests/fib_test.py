import unittest, Main
from Main.fib import fib_seq

class FibSeq(unittest.TestCase):
	def test_input_is_num(self):
		self.assertIsisnstace(fib_seq(b, int))

if __name__ == '__main__':
	unittest.main()