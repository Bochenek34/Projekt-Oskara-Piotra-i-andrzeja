from pydantic import BaseModel, EmailStr, Field, field_serializer
from typing import Union
from uuid import UUID

class TaxResidency(BaseModel):
    country_code: str = Field(min_length=2, max_length=2)
    region: str
    tax_id: str

class Investor(BaseModel):
    id: Union[UUID, str]
    email: EmailStr
    tier: int = Field(ge=1, le=5)
    tax_residency: TaxResidency
    private_key_hint: str

    @field_serializer("private_key_hint")
    def hide_private_key(self, v):
        return None
