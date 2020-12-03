[] Complete Category class in budget.

[x] Class should have an instance variable called ledger that is a list. 

[x] Class should have a deposit method. Accepts an amount and a description. Description should default to a empty string if none is provided. Appends a dict to ledger in the following format:
    {
        "amount": amount, 
        "description": description
    }

[x] Class should have a withdraw method. Works similarly to deposit but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds nothing should be added to ledger. Returns True if withdraw was successful, False otherwise.

[] Class should have a get_balance method. Returns current balance of budget based on deposits and withdrawals.

[] Class should have a transfer method. Accepts an amount and another budget category for arguments. Adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
Should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
If insufficient funds, add nothing to either ledger. 
Return True if transfer happened.
Return False otherwise.

[x] Class should have a check_funds method. Accepts an amount as an argument. Return False if amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both withdraw and transfer. 

When printed should print out in printed format.
    [] title line of 30 characters where name of the category is centered in a line of **** characters.
    [] list of items in ledger.
    [] description on the left, amount on the right.
    [] only first 23 characters of description should be displayed.
    [] Amount should contain two decimal places and max 7 characters.
    [] line displaying category total.


[] Create a function outside of the class called create_spend_chart which takes a list of categories as an argument and returns a string that is a bar chart.