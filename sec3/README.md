# Section 3 Exercises

## Bowl Class
```
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.flavors()  # returns a string of "chocolate, vanilla, coffee"
```

## Person and Bank Account Class
Use our existing Person and BankAccount classes.  Make it possible for a person to have one or more bank accounts.  So we can say:
```
p1.add_account(ba1)
p1.add_account(ba2)

p1.all_balances()           # returns a list of floats representing balances
p1.current_total_balance()  # gives the total balance across all accounts

p1.average_transaction_amount()  # returns the average amount of transactions across all accounts
```

## Shopping Cart Class
```
sc = ShoppingCart()
sc.add('book', 30, 1)    # name, price-per-unit, quantity
sc.add('toothbrush', 3, 4)

sc.remove('toothbrush')   # removes one toothbrush -- or removes
                            # the item altogether if the quantity is 0

sc.total()  # returns the total price of items in the shopping cart
```