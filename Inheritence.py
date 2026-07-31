class RBI:
    def interest_rate(self):
        print("Define interest rate as per your policy")

class SBI(RBI):
    def deposit(self):
        print("SBI Interest Rate is 5%")

class SBIHYDERABAD(SBI):
   def deposit(self):
       print("Deposit miney in SBI Hyderabad")

i = SBIHYDERABAD()
i.interest_rate()
