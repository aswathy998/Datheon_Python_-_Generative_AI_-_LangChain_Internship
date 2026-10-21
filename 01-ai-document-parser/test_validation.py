
from decimal import Decimal

from main import Invoice, validate_invoice_business_rules


def create_test_invoice(
    quantity=4,
    unit_price="125",
    line_total="500",
    subtotal="500",
    tax="25",
    total="525",
):
    return Invoice(
        invoice_number="TEST-002",
        invoice_date=None,
        due_date=None,
        supplier_name="Green Valley Supplies",
        supplier_email=None,
        customer_name="Bright Star Trading",
        items=[
            {
                "description": "Office chairs",
                "quantity": quantity,
                "unit_price": Decimal(unit_price),
                "line_total": Decimal(line_total),
            }
        ],
        subtotal=Decimal(subtotal) if subtotal is not None else None,
        tax_amount=Decimal(tax) if tax is not None else None,
        total_amount=Decimal(total) if total is not None else None,
        currency="AED",
        payment_status="unknown",
    )


# Test 1: Correct invoice should pass.
invoice = create_test_invoice()
validate_invoice_business_rules(invoice)
print("PASS: Correct invoice")

# Test 2: Zero quantity should fail.
try:
    invoice = create_test_invoice(quantity=0)
    validate_invoice_business_rules(invoice)
    print("FAIL: Zero quantity was accepted")
except ValueError:
    print("PASS: Zero quantity rejected")

# Test 3: Incorrect line total should fail.
try:
    invoice = create_test_invoice(line_total="400")
    validate_invoice_business_rules(invoice)
    print("FAIL: Incorrect line total was accepted")
except ValueError:
    print("PASS: Incorrect line total rejected")

# Test 4: Incorrect invoice total should fail.
try:
    invoice = create_test_invoice(total="600")
    validate_invoice_business_rules(invoice)
    print("FAIL: Incorrect invoice total was accepted")
except ValueError:
    print("PASS: Incorrect invoice total rejected")
