class Category:
    def __init__(self, category):
        self.category = category
        self.budget = 0
        self.ledger = []

    def check_funds(self, amount):
        if amount > self.budget:
            return False
        else:
            return True

    def deposit(self, amount, description=None):
        if description is None:
            description = ''
            self.budget += amount
            new_dict = {
                'description' : description,
                'amount' : amount
            }
            self.ledger.append(new_dict)
        else:
            self.budget += amount
            new_dict = {
                'description' : description,
                'amount' : amount
            }
            self.ledger.append(new_dict)

    def withdraw(self, amount, description=None):
        if self.check_funds:
            if description is None:
                description = ''
                self.budget -= amount
                new_dict = {
                    'description': description,
                    'amount' : 0 - amount
                }
                self.ledger.append(new_dict)
                return True
            else:
                self.budget -= amount
                new_dict = {
                    'description' : description,
                    'amount' : 0 - amount
                }
                self.ledger.append(new_dict)
                return True
        else:
            return False

    def get_balance(self):
        return self.budget

def create_spend_chart(categories):
    pass