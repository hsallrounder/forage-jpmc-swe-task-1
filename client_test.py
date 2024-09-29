import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))



  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_bidEqualsAsk(self):
    quotes = [
      {'top_ask': {'price': 120.5, 'size': 20}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.5, 'size': 100}, 'id': '0.109974697771', 'stock': 'XYZ'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),
                       (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], 120.5))

  def test_getDataPoint_zeroBidOrAsk(self):
    quotes = [
      {'top_ask': {'price': 0.0, 'size': 50}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 121.0, 'size': 30}, 'id': '0.109974697771', 'stock': 'LMN'},
      {'top_ask': {'price': 123.45, 'size': 10}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0.0, 'size': 15}, 'id': '0.109974697771', 'stock': 'OPQ'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))



if __name__ == '__main__':
    unittest.main()
