#income tax

income = float(input("Enter the gross income: "))
dependent = int(input("Enter the number of dependents: "))

total = income-10000-(dependent*3000)
tax = total*20/100

print('The income tax is:$', tax)