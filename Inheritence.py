class RBI:
    def interest_rate(self):
        print("Define interest rate as per your policy")

class SBI(RBI):
    def interest_rate(self):
        print("SBI Interest Rate is 5%")

class ICICI(SBI):
    def interest_rate(self):
        print("Rate of interest is 6%")
i = ICICI()
i.interest_rate()
