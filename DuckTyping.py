class Duck:
    def walk(self):
        print("Duck Walking")
class Human:
    def walk(self):
        print("Human Walking")
def display(obj):
    obj.walk()
display(Duck())
display(Human())