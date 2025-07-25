def converter(usd_val):
    inr_val = float(usd_val) * 75.0
    pkr_val = inr_val * 2.5
    return pkr_val
print("Enter the amount in USD:")
usd_input = input()
pkr_output = converter(usd_input)
print(f"{usd_input} USD = {pkr_output} PKR")
