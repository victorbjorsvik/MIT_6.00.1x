# Problem 1
def remainig_balance_month(balance, annualInterestRate, monthlyPaymentRate):
   
    for i in range(12):
        unpaid_balance = balance - (balance * monthlyPaymentRate)
        
        balance = round(unpaid_balance * (1 + annualInterestRate/12.0), 2)
        
    return balance
    
print(remainig_balance_month(balance,annualInterestRate,monthlyPaymentRate))

# Problem 2
def remainig_balance_month(balance, annualInterestRate, monthlyPaymentRate):
   
    for i in range(12):
        unpaid_balance = balance - (balance * monthlyPaymentRate)
        
        balance = round(unpaid_balance * (1 + annualInterestRate/12.0), 2)
        
    return balance
    
print(remainig_balance_month(balance,annualInterestRate,monthlyPaymentRate))

# Paste your code into this box
y = balance
epsilon = 1


MonthlyInterestRate = (annualInterestRate/12)
LowerBound = balance/12
UpperBound = (balance/12)*(1 + MonthlyInterestRate)**12


while abs(y) >= 0 + epsilon:
    bisection = (UpperBound + LowerBound)/2
    y = balance
    for i in range(12):
        unpaid_balance = y - bisection
        
        y = unpaid_balance * (1 + MonthlyInterestRate)

    if y < 0:
        UpperBound = bisection
    elif y > 0:
        LowerBound = bisection
   
print(round(bisection, 2))
