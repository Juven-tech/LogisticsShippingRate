# Shipping cost calculator

## Input Package weight and shipping rate
Weght = float(input("Enter the package weight in kilogrammes:"))
rate = float(input("Enter the shipping rate per kilogramme:"))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping cost: {shipping_cost} USD")
