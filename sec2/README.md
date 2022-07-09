# Section 2 Exercises

## Scoop class
Each instance is one scoop of ice cream

```
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)  # chocolate

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)  # chocolate, vanilla, coffee
```

## Person class
Mame, e-mail address, and phone number

Create several people, and iterate over them in a list and print their names (similar to a phone book)

Change the e-mail address of one person, and show that it has changed by printing your list a second time

## Create a BankAccount class
It'll have a single attribute (per instance), transactions -- a list of floats

Every time you deposit, append a positive float
Every time you withdraw, append a negative float

(a) create two different accounts
(b) add a number of transactions +/- to each account
(c) show, for each account, the number of transactions and the average amount per transaction, as well as the current balance.  (assume it starts at 0)