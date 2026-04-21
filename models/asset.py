from pydantic import BaseModel, Field, computed_field
from enum import Enum
from decimal import Decimal
from datetime import datetime

class AssetType(str, Enum):
    CRYPTO="CRYPTO"
    STOCK="STOCK"
    COMMODITY="COMMODITY"

class TradeAction(str, Enum):
    BUY="BUY"
    SELL="SELL"

class Asset(BaseModel):
    asset_type: AssetType
    quantity: Decimal = Field(gt=0)
    last_sync: datetime
    trade_action: TradeAction

    @computed_field
    @property
    def volatility_score(self)->str:
        if self.asset_type == AssetType.CRYPTO and self.quantity > 10:
            return "Extreme"
        elif self.quantity > 5:
            return "Stable"
        return "Low"
