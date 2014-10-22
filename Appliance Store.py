## function unitsInput reads the inputs and returns a list of
## the quantities sold in each category     
def inputUnits():
    quantities = [] #Create a list to store the numbers of apliance
    print 'Please input the quantity of each appliance.'
    
    #Ask user to input the number of stoves
    #Then append the number to the list we create
    number = int(raw_input('Number of Stoves: '))
    quantities.append(number)
    
    number = int(raw_input('Number of Computers: '))
    quantities.append(number)
    
    number = int(raw_input('Number of Refrigerators : '))
    quantities.append(number)

    number = int(raw_input('Number of Washer/Dryer Bundles: '))
    quantities.append(number)
    
    return quantities
        
## function commissionStove calculates and returns the
## commission of stoves sold
def calcStoveCommission(units):
    if units < 3:
        commission = 0
    else:
        commission = units * 1400 * 0.03
        if units > 8:
            commission = commission + 200
    return commission

## function commissionComputer calculates and returns the
## commission of compurers sold
def calcComputerCommission(units):
    if units < 15:
        commission = 0
    else:
        commission = units * 600 * 0.025
        if units > 30:
            commission = commission + 500
    return commission

## function commissionRefrigerator calculates and returns the
## commission of refrigerators sold
def calcRefrigeratorCommission(units):
    if units < 5:
        commission = 0
    else:
        commission = units * 1200 * 0.035
        if units > 12:
            commission = commission + 250
    return commission

## function commissionWDBundle calculates and returns the
## commission of washers&dryers sold
def calcWDBundleCommission(units):
    if units < 5:
        commission = 0
    else:
        commission = units * 1200 * 0.04
        if units > 12:
            commission = commission + 300
    return commission

##Use all the functions to calculate and print commissions
quantities = inputUnits()

print '---------------- Commission ----------------'
##totalQuantity is used to decide if there should be an extra bonus of 1000
totalQuantity = 0

##quantities[0] is the number of stoves
comStove = calcStoveCommission(quantities[0])
##Add the quantity of stoves to totalQuantity
totalQuantity = totalQuantity + quantities[0]
print 'Commission for Stove: ', comStove

##quantities[1] is the number of computers
comComputer = calcComputerCommission(quantities[1])
##Add the quantity of computers to totalQuantity
totalQuantity = totalQuantity + quantities[1]
print 'Commission for Computer: ', comComputer

##quantities[2] is the number of refrigerators
comRefrigerator = calcRefrigeratorCommission(quantities[2])
##Add the quantity of refrigerators to totalQuantity
totalQuantity = totalQuantity + quantities[2]
print 'Commission for Refrigerator: ', comRefrigerator

##quantities[3] is the number of W/D bundles
comWDBundle = calcWDBundleCommission(quantities[3])
##Add the quantity of W/D bundles to totalQuantity
totalQuantity = totalQuantity + quantities[3]
print 'Commission for WDBundle: ', comWDBundle

##Get the total commission
totalCommission = comStove + comComputer + comRefrigerator + comWDBundle
##if totalQuantity is larger than 100
##there is an extra bonus of 1000
if totalQuantity > 100:
    totalCommission = totalCommission + 1000
    print 'Extra Bonus:', 1000
    
print 'Total Commission:', totalCommission
        
                      
