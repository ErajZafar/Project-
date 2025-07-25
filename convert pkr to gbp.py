# Conversion rate (example: 1 GBP = 360 PKR)
PKR_TO_GBP_RATE = 1 / 360  # 1 PKR = 0.00278 GBP

def pkr_to_gbp(pkr_amount):
    return pkr_amount * PKR_TO_GBP_RATE

try:
    pkr = float(input("Enter amount in PKR: "))
    gbp = pkr_to_gbp(pkr)
    print(f"{pkr} PKR = {gbp:.2f} GBP")
except ValueError:
    print("Please enter a valid number.")