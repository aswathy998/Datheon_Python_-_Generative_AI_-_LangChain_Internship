
from decimal import Decimal

import pytest

from main import Invoice, validate_invoice_business_rules


def make_invoice(quantity=2, unit_price="150", line_total="300",
                 subtotal="300", tax="15", total="315"):
    return Invoice(
        invoice_number="TEST-003",
        invoice_date=None,
        due_date=None,
        supplier_name="Example Supplier",
        supplier_email=None,
        customer_name="Example Customer",
        items=[
            {
                "description": "Laptop accessories",
                "quantity": quantity,
                "unit_price": Decimal(unit_price),
                "line_total": Decimal(line_total),
            }
        ],
        subtotal=Decimal(subtotal),
        tax_amount=Decimal(tax),
        total_amount=Decimal(total),
        currency="AED",
        payment_status="unpaid",
    )


def test_valid_invoice_passes():
    invoice = make_invoice()
    validate_invoice_business_rules(invoice)


def test_zero_quantity_fails():
    invoice = make_invoice(quantity=0)

    with pytest.raises(ValueError):
        validate_invoice_business_rules(invoice)


def test_wrong_line_total_fails():
    invoice = make_invoice(line_total="250")

    with pytest.raises(ValueError):
        validate_invoice_business_rules(invoice)


def test_wrong_invoice_total_fails():
    invoice = make_invoice(total="400")

    with pytest.raises(ValueError):
        validate_invoice_business_rules(invoice)
