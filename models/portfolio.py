from pydantic import BaseModel
from typing import List
from models.asset import Asset

class Portfolio(BaseModel):
    assets: List[Asset]

    @property
    def total_market_exposure(self):
        return sum(a.quantity for a in self.assets)
