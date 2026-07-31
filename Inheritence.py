class RBI:
    def interest_rate(self):
        print("Define interest rate as per your policy")

class SBI(RBI):
    def deposit(self):
        print("SBI Interest Rate is 5%")

class ICICI(RBI):
   def deposit(self):
       print("Deposit miney in SBI Hyderabad")

class HDFC(RBI):
    def interest_rate(self):
        print("HDFC Interest Rate is 8%")

s = SBI()
s.interest_rate()

i = ICICI()
i.interest_rate()

h = HDFC()
h.interest_rate()

