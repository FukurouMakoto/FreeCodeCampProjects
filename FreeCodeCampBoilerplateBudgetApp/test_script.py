from budget import Category
from budget import get_percentage, get_percentage_string, get_deposit_sum, get_withdraw_sum, get_new_balance, compose_string_list, make_string, create_spend_chart

food = Category('food')
food.deposit(1000.00, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'resturant and more food')
food.withdraw(50.00, 'Clothing')
food.withdraw(300.00, 'big grocery shopping')
food.withdraw(150.00, 'night out with friends')
#new_balance = get_deposit_sum(food)
#old_balance = new_balance - get_withdraw_sum(food)

#print(food)

swooby_booby = create_spend_chart(food, food.category)
for line in swooby_booby:
    print(line)
