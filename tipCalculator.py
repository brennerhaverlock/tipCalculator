# calculate tip
def calculateTax(cost, percentageTax):
return (cost * (percentageTax / 100))


def calculateCost(cost, percentageTip):
return (cost * (percentageTip / 100))
# Ask user for the cost

cost = float(input("Enter cost of bill(Exclude $ sign) \n"))

# Ask user for tax percentage
percentageTax = int(input("Enter a tax percentage (Exclude % sign)\n "))


# Ask user for tip percentage

# Return cost multiplied by tax percentage

