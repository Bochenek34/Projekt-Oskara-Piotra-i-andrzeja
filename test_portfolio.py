import unittest
from datetime import datetime
from models.asset import Asset
from models.portfolio import Portfolio


class TestPortfolio(unittest.TestCase):

    def test_total_market_exposure(self):
        assets = [
            Asset(quantity=10, asset_type="STOCK", last_sync=datetime.now(), trade_action="BUY"),
            Asset(quantity=20, asset_type="STOCK", last_sync=datetime.now(), trade_action="BUY"),
            Asset(quantity=5, asset_type="STOCK", last_sync=datetime.now(), trade_action="BUY"),
        ]
        portfolio = Portfolio(assets=assets)

        self.assertEqual(portfolio.total_market_exposure, 35)


if __name__ == "__main__":
    unittest.main()