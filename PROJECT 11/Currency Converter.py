with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = float(parsed[1].strip())  # store as float

amount = int(input("Enter the amount to convert : "))

print("Enter the name of currency you want to convert this amount to:\nAvailable Options:\n")

# print all available currency names
for item in currencyDict.keys():
    print(item)

currency = input("Please enter one of these values : ")

print(f"{amount} INR is equal to {amount * currencyDict[currency]} {currency}")
