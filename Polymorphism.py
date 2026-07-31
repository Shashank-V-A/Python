class Rbi:
    def interest_rate(self):
        print("As per the Bank policy:")
class Sbi:
    def interest_rate(self):
        print("Interest rate 5%")
banks = [Rbi(), Sbi()]

for a in banks:
    a.interest_rate()
    