##Commented-out print statments are for debugging. 

print("Use at your own risk. Creator not responsible for anything. Please see README.md")

number = input("Amount here (dollars only): ")
amount = int(number.replace(",",""))
float_amount = float(amount)
##print(float_amount)

bond = str(float_amount*0.4)
##print(printbond)

reit = str(float_amount*0.06)
##print(printreit)

stocks = str(float_amount*0.54)
##print(printstocks)

intl = str(float_amount*0.18)
##print(printintl)

totstock = str(float_amount*0.36)
##print(printtotstock)

print("For Bond fund (40% of total): " + bond)
print("For REIT fund (6% of total): " + reit)
print("For International fund: (18% of total): " + intl)
print("For Total Stock fund (36% of total): " + totstock)
print("(For Stocks overall (54% of total): " + stocks + ")")
print("More info at: https://www.bogleheads.org/forum/viewtopic.php?t=10413")
