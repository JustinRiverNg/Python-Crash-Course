# The unittest module is used for testing
import unittest
from name_function import get_formatted_name

# Create a class for the series of tests for this function
class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self): # Create a method for this test
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin') # Calling the function
		self.assertEqual(formatted_name, 'Janis Joplin') # Compares the result

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang', 
			'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main() # Tells python to run the tests in this file
