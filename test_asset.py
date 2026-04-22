import unittest
from decimal import Decimal
from datetime import datetime

from pydantic import ValidationError

from models.asset import Asset, AssetType, TradeAction


class TestAssetModel(unittest.TestCase):

    def test_valid_asset_creation(self):
        asset = Asset(
            asset_type=AssetType.CRYPTO,
            quantity=Decimal("1"),
            last_sync=datetime.utcnow(),
            trade_action=TradeAction.BUY,
        )

        self.assertEqual(asset.asset_type, AssetType.CRYPTO)
        self.assertEqual(asset.quantity, Decimal("1"))
        self.assertEqual(asset.trade_action, TradeAction.BUY)

    def test_quantity_must_be_greater_than_zero(self):
        with self.assertRaises(ValidationError):
            Asset(
                asset_type=AssetType.STOCK,
                quantity=Decimal("0"),
                last_sync=datetime.utcnow(),
                trade_action=TradeAction.SELL,
            )

        with self.assertRaises(ValidationError):
            Asset(
                asset_type=AssetType.STOCK,
                quantity=Decimal("-5"),
                last_sync=datetime.utcnow(),
                trade_action=TradeAction.SELL,
            )

    def test_volatility_score_extreme(self):
        asset = Asset(
            asset_type=AssetType.CRYPTO,
            quantity=Decimal("11"),
            last_sync=datetime.utcnow(),
            trade_action=TradeAction.BUY,
        )
        self.assertEqual(asset.volatility_score, "Extreme")

    def test_volatility_score_stable(self):
        asset = Asset(
            asset_type=AssetType.STOCK,
            quantity=Decimal("6"),
            last_sync=datetime.utcnow(),
            trade_action=TradeAction.BUY,
        )
        self.assertEqual(asset.volatility_score, "Stable")

    

   


if __name__ == "__main__":
    unittest.main()