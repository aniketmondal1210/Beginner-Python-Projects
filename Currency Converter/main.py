from currency_converter import CurrencyConverter

c = CurrencyConverter() #Create a Currency Converter Object
amount = input("Enter the amount: ")
from_currency = input("From which currency: ") 
to_currency = input("To which currency: ")
converted_amount = c.convert(amount,from_currency,to_currency)

print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
