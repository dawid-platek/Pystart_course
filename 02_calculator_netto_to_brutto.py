netto_price = float(input("Enter the net price: "))
vat_rate = 0.23  # VAT rate of 23%
brutto_price = netto_price * (1 + vat_rate)  # Calculate gross price
print(f"The gross price is: {brutto_price:.2f}")  # Print gross price rounded to two decimal places