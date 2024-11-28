import os

import mojito
import pprint
from dotenv import load_dotenv
from typing import Optional
from enum import Enum

class Favorites(Enum):
	삼성전자 = "005930"


# load .env
load_dotenv()

class Sentinel():
	def __init__(self):
		API_KEY = os.environ.get('API_KEY')
		API_SECRET = os.environ.get('API_SECRET')
		ACC_NUM = os.environ.get('ACC_NUM')

		self.broker = mojito.KoreaInvestment(
		    api_key=API_KEY,
		    api_secret=API_SECRET,
		    acc_no=ACC_NUM
		)

	def get_price(self, symbol):
		resp = self.broker.fetch_price(symbol)
		return resp["output"]["stck_prpr"]

	def get_deposit(self):
		resp = self.broker.fetch_balance()
		return resp["output2"]["dcna_tot_amt"]

	def buy_stock(self, symbol: str, price: Optional[int] = None, quantity: int = 1):
		if price is None:
			resp = self.broker.create_market_buy_order(
						    symbol=symbol,
						    quantity=quantity
						)
		else:
			resp = self.broker.create_limit_buy_order(
						    symbol=symbol,
						    price=price,
						    quantity=quantity
						)

		pprint.pprint(resp)

	def sell_stock(self, symbol: str, price: Optional[int] = None, quantity: int = 1):
		if price is None:
			resp = self.broker.create_market_sell_order(
						    symbol=symbol,
						    quantity=quantity
						)
		else:
			resp = self.broker.create_limit_sell_order(
						    symbol=symbol,
						    price=price,
						    quantity=quantity
						)
		pprint.pprint(resp)
