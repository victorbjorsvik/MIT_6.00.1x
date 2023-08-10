## Remaing balance after a year ##

def remainig_balance_month (balance, annualInterestRate, monthlyPaymentRate):
    for i in range(1,13):
        unpaid_balance = balance - (balance * monthlyPaymentRate)
        
        balance = unpaid_balance * (1 + annualInterestRate/12.0)**i
        
        print("Balance is %i." % balance)
        
    return round(balance, 2)

remainig_balance_month(42, 0.2, 0.04)


    
    

   
    
    
   
    