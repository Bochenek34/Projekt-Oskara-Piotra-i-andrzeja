import unittest
from uuid import uuid4
from pydantic import ValidationError

from models.investor import Investor, TaxResidency


class TestInvestor(unittest.TestCase):

    def setUp(self):
        self.tax = TaxResidency(
            country_code="PL",
            region="Mazowieckie",
            tax_id="123"
        )

    def base_investor(self, **overrides):
        data = {
            "id": str(uuid4()),
            "email": "test@example.com",
            "tier": 2,
            "tax_residency": self.tax,
            "private_key_hint": "secret",
        }
        data.update(overrides)
        return Investor(**data)

    def test_valid_investor(self):
        inv = self.base_investor()
        self.assertEqual(inv.tier, 2)
        self.assertEqual(inv.email, "test@example.com")

    def test_invalid_tier_low(self):
        with self.assertRaises(ValidationError):
            self.base_investor(tier=0)

    def test_invalid_tier_high(self):
        with self.assertRaises(ValidationError):
            self.base_investor(tier=10)

    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            self.base_investor(email="bad-email")

    def test_invalid_country_code(self):
        with self.assertRaises(ValidationError):
            TaxResidency(
                country_code="POL",
                region="Mazowieckie",
                tax_id="123"
            )

   

if __name__ == "__main__":
    unittest.main()