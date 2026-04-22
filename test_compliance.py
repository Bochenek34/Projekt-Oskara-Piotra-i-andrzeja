import unittest
from datetime import date, timedelta
from models.compliance import Compliance, ComplianceStatus


class TestCompliance(unittest.TestCase):

    def test_valid_compliance(self):
        issue = date(2024, 1, 1)
        expiry = issue + timedelta(days=100)  # więcej niż 90 dni

        compliance = Compliance(
            license_key="ABCDEFGHIJKL",  # 12 znaków
            issue_date=issue,
            expiry_date=expiry,
            compliance_status=ComplianceStatus.COMPLIANT
        )

        self.assertEqual(compliance.license_key, "ABCDEFGHIJKL")
        self.assertEqual(compliance.compliance_status, ComplianceStatus.COMPLIANT)


if __name__ == "__main__":
    unittest.main()