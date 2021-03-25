CURRENT_YEN_TO_EUR_EXCHANGE_RATE = 0.0080

def yen_to_euro(yen):
    value_in_euro = yen * CURRENT_YEN_TO_EUR_EXCHANGE_RATE
    return value_in_euro

yen = float(input("Welcome to money convertor.\nHow many yens do you want to convert? "))
value_in_euro = yen_to_euro(yen)
print("\n\n")
print(f"The exchange rate for today is:\n{yen} yen = {value_in_euro} euro")