class Customer(object):


    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


erik = Customer('erik eastham',100)
print erik.name
print erik.balance
erik.balance = 1000
print erik.balance
Customer.deposit(erik,100)
#providing two arguments here, so that you apply the deposit method to erik,
#and the amount is of 100
print erik.balance

erik.withdraw(100)
#shorthand is erik.deposit(100)
#customer.deposit(self,balance) = self.deposit(balance) - moving the self outside for shorthand
print erik.balance
