# Problem 4: Income Tax
# This program calculates adjusted gross income, taxable income, tax, and refund or amount due.

# These constants store deduction amounts and the AGI limit.
SINGLE_DEDUCTION = 12000
MARRIED_DEDUCTION = 24000
AGI_LIMIT = 120000

# Read income, filing status, and taxes withheld.
print("Enter wages, taxable interest, unemployment compensation, filing status, and taxes withheld.")
print("Use 1 for single or 2 for married.")
print("Example: 80000 0 500 2 12000")
wages, interest, unemployment, status, withheld = input("Tax information: ").split()
wages = int(wages)
interest = int(interest)
unemployment = int(unemployment)
status = int(status)
withheld = int(withheld)

# Calculate and display adjusted gross income.
agi = wages + interest + unemployment
print(f"AGI: ${agi:,}")

# Stop the program if income is too high for this tax form.
if agi > AGI_LIMIT:
    print("Error: Income too high to use this form")
else:
    # Use single status if the user did not enter 1 or 2.
    if status != 1 and status != 2:
        status = 1

    # Choose the correct deduction for the filing status.
    if status == 2:
        deduction = MARRIED_DEDUCTION
    else:
        deduction = SINGLE_DEDUCTION

    # Taxable income cannot be negative.
    taxable_income = agi - deduction
    if taxable_income < 0:
        taxable_income = 0

    # Calculate federal tax for a single filer.
    if status == 1:
        if taxable_income <= 10000:
            federal_tax = taxable_income * 0.10
        elif taxable_income <= 40000:
            federal_tax = 1000 + (taxable_income - 10000) * 0.12
        elif taxable_income <= 85000:
            federal_tax = 4600 + (taxable_income - 40000) * 0.22
        else:
            federal_tax = 14500 + (taxable_income - 85000) * 0.24

    # Calculate federal tax for a married filer.
    else:
        if taxable_income <= 20000:
            federal_tax = taxable_income * 0.10
        elif taxable_income <= 80000:
            federal_tax = 2000 + (taxable_income - 20000) * 0.12
        else:
            federal_tax = 9200 + (taxable_income - 80000) * 0.22

    # Round federal tax to the nearest whole dollar.
    federal_tax = round(federal_tax)

    # Calculate whether the taxpayer owes money or gets a refund.
    tax_due = federal_tax - withheld

    # Display deduction, taxable income, and federal tax.
    print(f"Deduction: ${deduction:,}")
    print(f"Taxable income: ${taxable_income:,}")
    print(f"Federal tax: ${federal_tax:,}")

    # Display tax due or refund as a positive value.
    if tax_due >= 0:
        print(f"Tax due: ${tax_due:,}")
    else:
        print(f"Tax refund: ${abs(tax_due):,}")
