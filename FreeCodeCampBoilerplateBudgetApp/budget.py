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
        if self.check_funds(amount):
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

    def transfer(self, amount, category):
        if self.check_funds(amount):
            descrip = f'Transfer to {category.category}'
            self.withdraw(amount, descrip)
            descrip = f'Transfer from {self.category}'
            category.deposit(amount, descrip)
            return True
        else:
            return False

    def __str__(self):
        balance = 0
        transactions = []
        nl = '\n'
        header = self.category.center(30, '*')
        for item in self.ledger:
            transaction = item['amount']
            balance += transaction
            item['amount'] = '{:.2f}'.format(item['amount'])
            description = '{:<23}'.format(item['description'])
            amount = '{:>7}'.format(item['amount'])
            transactions.append(f'{description}{amount}')
        total = f'Total: {balance}'
        return f"{header}\n{nl.join(tuple(transactions))}\n{total}"

def create_spend_chart():
    pass


food = Category('Food')
food.deposit(1000, 'Payday')
food.withdraw(50, 'groceries')
food.withdraw(175, 'dinner out with friends')
food.withdraw(50, 'bacon, eggs, vegetables, fruits and salad for breakfast')
print(food)


''' THIS IS THE ORIGINAL VERSION OF THE CODE
def __str__(self):
        balance = 0
        transactions = []
        nl = '\n'
        header = self.category.center(30, '*')
        for item in self.ledger:
            transaction = item['amount']
            balance += transaction
            item['amount'] = '{:.2f}'.format(item['amount'])
            transactions.append(f"{item['description']:<23}{item['amount']:>7}")
        total = f'Total: {balance}'
        return f"{header}\n{nl.join(tuple(transactions))}\n{total}"
'''