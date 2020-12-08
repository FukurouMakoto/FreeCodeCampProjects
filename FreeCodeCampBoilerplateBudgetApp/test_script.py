from budget import Category
from budget import get_percentage, get_percentage_string, get_deposit_sum, get_withdraw_sum, get_new_balance, compose_string_list, make_string, create_spend_chart, print_spend_chart
import pprint
food = Category('Food')
food.deposit(1000.00, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'resturant and more food')
food.withdraw(50.00, 'Clothing')
food.withdraw(300.00, 'big grocery shopping')
food.withdraw(150.00, 'night out with friends')

Clothes = Category('Clothing')
Clothes.deposit(2000.00, 'initital deposit')
Clothes.withdraw(800.00, 'bought clothes for work')
Clothes.withdraw(200.00, 'work uniform')
Clothes.withdraw(150.00, 'bought new sneakers')

Auto = Category('Auto')
Auto.deposit(10000.00, 'initial deposit')
Auto.withdraw(5000.00, 'repair after accident')
Auto.withdraw(500.00, 'new bumper plates')
Auto.withdraw(300.00, 'new tires')
#new_balance = get_deposit_sum(food)
#old_balance = new_balance - get_withdraw_sum(food)

#print(food)
category_list = [food, Clothes, Auto]
print_spend_chart(create_spend_chart(category_list))

'''
for line in fuck_around[1:11]:
    print(line)
for line in shit_around[1:11]:
    print(line)
'''




