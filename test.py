import unittest

from webscraping import getRevenue, getOperatingIncome,getNetIncome,getTotalAssets,getTotalEquity
page_link='https://en.wikipedia.org/wiki/Tesla,_Inc.'

class TestRevenue(unittest.TestCase):
	def test_Revenue(self):
		"""Test if the revenue is giving the expected value in CHR"""
		
		result = getRevenue(page_link)
		print(result)
		self.assertEqual(result, "138.896 billion")

class TestOperatingIncome(unittest.TestCase):
		
	def test_OperatingIncome(self):
		"""Test if the Operation Income is giving the expected value in CHR"""

		result = getOperatingIncome(page_link)
		print(result)
		self.assertEqual(result, "2.511 billion")

class TestNetIncome(unittest.TestCase):
		
	def test_TestNetIncome(self):
		"""Test if the Net Income is giving the expected value in CHR"""

		result = getNetIncome(page_link)
		print(result)
		self.assertEqual(result, "6.317 billion")

class TestTotalAssets(unittest.TestCase):
		
	def test_TotalAssets(self):
		"""Test if the Total Assets is giving the expected value in CHR"""

		result = getTotalAssets(page_link)
		print(result)
		self.assertEqual(result, "192.477 billion")
		
class TestTotalEquity(unittest.TestCase):
	def test_TotalEquity(self):
		"""Test if the Total Equity is giving the expected value in CHR"""

		result=getTotalEquity(page_link)
		print(result)
		self.assertEqual(result, "31.862 billion")

if __name__ == '__main__':
    unittest.main()
