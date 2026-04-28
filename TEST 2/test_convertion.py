import unittest
import convertion
class TestConvertion(unittest.TestCase):
	def test_test_exchange_works(self):
		convertion.naira_exchange(1.2)
	def test_test_convertion_returns_correct_result_with_a_float_digit(self):
		actual = convertion.naira_exchange(1.2)
		expected = 1860.0
		self.assertEqual(actual, expected)
	def test_test_convertion_returns_correct_result_with_a_int_digit(self):
		actual = convertion.naira_exchange(1)
		expected = 1550
		self.assertEqual(actual, expected)
	def test_test_convertion_returns_invalid_data_type_with_wrong_input(self):
		actual = convertion.naira_exchange("goal")
		expected = "invalid input"
		self.assertEqual(actual, expected)

