"""
The rules with self are that

Any instance data should be prepended with self

e.g., the earn method references self.wealth rather than just wealth
Any method defined within the class should have self as its first argument

e.g., def earn(self, y) rather than just def earn(y)
Any method referenced within the class should be called as self.method_name
"""


class Consumer:
    def __init__(self, w):
        "Initialize consumer with w dollars of wealth"
        self.wealth = w

    def earn(self, y):
        """
        The consumer earns y dollars
        """
        self.wealth += y

    def spend(self, x):
        """
        The consumer spends x dollars if feasible
        """
        new_wealth = self.wealth - x
        if new_wealth < 0:
            print("Insufficent funds")
        else:
            self.wealth = new_wealth

c1 = Consumer(100)
c1.spend(10)
print(c1.wealth)
# attach new attributes
# c1.wealth = 1

print(Consumer.__dict__)  # Show __dict__ attribute of class object

