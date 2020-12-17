from itertools import zip_longest
class Category:
    def __init__(self, category):
        self.category = category
        self.budget = 0
        self.ledger = []
        #self.budget_used = 0
        #self.percentage_spent = 0

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
        total = f'Total: {int(balance):.2f}' #creates a fstring for the balance total
        return f"{header}\n{nl.join(tuple(transactions))}\n{total}" #returns a completed fstring for each item in list.
        #note that because we need to return a list of strings, we can use nl.join(tuple(list)) in order
        #release each item in the list as a string. Python can unpack tuples at runtime.



#Non-class functions
def create_spend_chart_mine(category_list):
    if isinstance(category_list, list):
        for item in category_list:
            return compose_chart(item)
    elif isinstance(category_list, Category):
        return compose_chart(category_list)
    else:
        raise Exception("Invalid item...")

def print_spend_chart(charts):
    for line in charts:
        print(line)

def compose_chart(Category): #Will need to be composed of different parts
    deposits = get_deposit_sum(Category)
    withdraws = get_withdraw_sum(Category)
    balance = get_new_balance(deposits, withdraws)
    percentage = get_percentage_string(get_percentage(balance, deposits))
    category = Category.category
    return compose_string_list(percentage, category)


def get_percentage(new, old): #return percentage in decimal format
    if new == old:
        return 100
    try: 
        return (abs(new-old) / old * 100)
    except ZeroDivisionError:
        return 0

def get_percentage_string(num): #You call get_percentage with your values as an argument in this function.
    return f'{round(num, -1)}' #rounds down to nearest tenth place
#I need to add all the positive values in the ledger and all the negative values in the ledger in order to get the difference between the two. Then I can feed those values into get percentage.

def get_deposit_sum(Category): #Returns all deposits
    return int(sum([x['amount'] for x in Category.ledger if float(x['amount']) > 0]))

def get_withdraw_sum(Category): #Returns all withdrawals
    return int(abs(sum([x['amount'] for x in Category.ledger if float(x['amount']) < 0])))

def get_new_balance(num1, num2): #Feed get_deposit_sum and get_withdraw_sum in that order for balance after all withdrawls
    return num1 - num2

#I will need to find a way to create custom made strings that will contain the necessary 
#information; variables for each line.

def compose_string_list(num, category):
    status_strings = []
    percentage = 100
    status_strings.append('Percentage spent by category'.ljust(30))
    while percentage >= 0:
        status_strings.append(make_string(num, percentage))
        percentage -= 10
    status_strings.append('')
    status_strings.append('-' * 30)
    for letter in category:
        status_strings.append('     ' + letter)
    return status_strings    

def create_bars(num, percentage):
    return f"{'o' if percentage <= float(num) else ' '}"   

def make_string(num, percentage):
    if percentage == 0:
        return f"{'  '+ str(percentage)}| {create_bars(num, percentage)}".ljust(30)
    elif percentage < 100 and percentage > 0:
        return f"{' '+ str(percentage)}| {create_bars(num, percentage)}".ljust(30)
    else:
        return f"{percentage}| {create_bars(num, percentage)}".ljust(30)

def get_percentage_spent(Category):
    deposits = get_deposit_sum(Category)
    withdraws = get_withdraw_sum(Category)
    balance = get_new_balance(deposits, withdraws)
    percentage = get_percentage(balance, deposits)
    return round(percentage, -1)

def chart_string(cat:Category):
    num_os = int((get_percentage_spent(cat)) / 10 + 1)
    os = "o" * num_os
    return os.rjust(11) + '-' + cat.category

def create_spend_chart(categories):
    filler = "\n".ljust(12) + "-\n"
    wide_string = filler.join([chart_string(c) for c in categories])
    data = [''.join(s) for s in zip_longest(*wide_string.split('\n'), fillvalue=" ")]
    y_axis = [str(p).rjust(3) + "|" for p in range(100, -1, -10)]
    chart = "\n".join([
        ax + d 
        for ax, d in zip_longest(y_axis, data, fillvalue="    ")
    ])
    return chart 
'''
maybe set a variable here that is equal to {'o', if percentage...}, and multiply it 
by the len of list?
Need to figure out some way where I can work the make string function into taking 
a number and multiply create_bars by it. Maybe by putting them in a list?
I cannot pass in a simple len(list). I need to find a way where I can tell
python to not only do create_bars for every item in the list, 
but to do it for each item in the list.
I think I need to look into making some of these functions into class options instead. 
That might help not only to make the code work but also make it cleaner.
'''