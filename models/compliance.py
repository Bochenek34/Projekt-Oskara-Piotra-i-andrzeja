from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import date, timedelta

class ComplianceStatus(str, Enum):
    COMPLIANT="COMPLIANT"
    FLAG_RED="FLAG-RED"
    UNDER_REVIEW="UNDER-REVIEW"

class Compliance(BaseModel):
    license_key: str = Field(min_length=12, max_length=12)
    issue_date: date
    expiry_date: date
    compliance_status: ComplianceStatus

    @model_validator(mode="after")
    def validate_dates(self):
        if self.expiry_date < self.issue_date + timedelta(days=90):
            raise ValueError("Expiry date must be at least 90 days later")
        return self
