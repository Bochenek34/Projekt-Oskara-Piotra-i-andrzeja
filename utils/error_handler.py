from pydantic import ValidationError

def parse_errors(e: ValidationError):
    errors=[]
    for err in e.errors():
        field = err["loc"][0] if err.get("loc") else "unknown"
        if field == "asset_type":
            msg = "Invalid Asset Type. Supported types are: CRYPTO, STOCK, COMMODITY"
        else:
            msg = err["msg"]
        errors.append({"loc": field, "msg": msg})
    return errors
