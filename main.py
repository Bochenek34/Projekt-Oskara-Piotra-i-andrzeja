from models.asset import Asset
from pydantic import ValidationError
from utils.error_handler import parse_errors

try:
    asset = Asset(
        asset_type="BTC",
        quantity="0.00054",
        last_sync="2026-04-19T12:00:00",
        trade_action="BUY"
    )
    print(asset.model_dump())
except ValidationError as e:
    print(parse_errors(e))
