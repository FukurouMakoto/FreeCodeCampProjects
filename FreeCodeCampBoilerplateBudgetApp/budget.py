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
        balance = 0 #to uptick and collect correct balance
        transactions = [] # to hold transaction log strings
        nl = '\n' #cannot place newlines in fstrings
        header = self.category.center(30, '*') #for first line.
        #center(string length, what to fill it with) creates a centered string with "title"
        for item in self.ledger:
            transaction = item['amount'] #needed because past this loop amount stores as string
            balance += transaction #uptick balance with each transaction amount.
            item['amount'] = '{:.2f}'.format(item['amount']) #amount is formatted to two decimal places.
            description = item['description'][:23] #truncate item desciption to max 23 characters
            amount = item['amount'][:7] #truncate amount description to max 7 characters
            transactions.append(f'{description:<23}{amount:>7}') #Append a f string to fit to 30 characters total
        total = f'Total: {balance}' #creates a fstring for the balance total
        return f"{header}\n{nl.join(tuple(transactions))}\n{total}" #returns a completed fstring for each item in list.
        #note that because we need to return a list of strings, we can use nl.join(tuple(list)) in order
        #release each item in the list as a string. Python can unpack tuples at runtime.
def create_spend_chart(Categories):
    print("Percentage spent by category")


def get_percentage(new, old):
    if new == old:
        return 100
    try: 
        return (abs(new-old) / old * 100)
    except ZeroDivisionError:
        return 0

def get_percentage_string(num): #You call get_percentage with your values as an argument in this function.
    return f'{round(num, -1)}%' #rounds down to nearest tenth place
#I need to add all the positive values in the ledger and all the negative values in the ledger in order to get the difference between the two. Then I can feed those values into get percentage.

def get_deposit_sum(Category):
    return int(sum([x['amount'] for x in Category.ledger if x['amount'] > 0]))

def get_withdraw_sum(Category):
    return int(abs(sum([x['amount'] for x in Category.ledger if x['amount'] < 0])))



