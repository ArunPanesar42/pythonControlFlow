# Control Flow in Python

## IF STATEMENTS

### What are if statements 

- Decision-making is required when we want to execute a code only if a certain condition is satisfied, the if/elif/else statement is used in Python for decision-making.
### These are the statements in action 
```python
age = 16
if age >= 15:  # If the the user is above the age of 15, allow them to buy a ticket
    print("Thank you, Please proceed to your purchase ")
elif age < 15:  # If the the user is not above the age of 15, do not allow them to buy a ticket
    print(" You may not pass")
else:  # anything else happens and no conditions are met, return this
    print("Something, went wrong, please try again later!")
```

## Loops

#### Loops help us iterate through data 

### What are FOR loops?

-The "for" loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
-Iterating over a sequence is called traversal.
- We made a shopping list to iterate through 
```python
shopping_list = ["bread", "eggs", "milk", "orange"]

# Lets for loop to iterate through our shopping list
for items in shopping_list:
    print(items)
```
- We can also go through the loop until we find an item using `break`
```python
for items in shopping_list:
    print(items)
    if items == "milk":
        break   # At this point when we find milk the program will "break" meaning the loop ends
```
- We also iterated through  dictionaries using our food bill
- Here is our Created Bill 
```python
food_bill = {1: {"name": "James", "bill": "£1"}, 2: {"name": " Bond", "bill": "£2"}
    , 3: {"name": "shah", "bill": "£3"}}
```
- this is how we iterate through
```python
for items in food_bill.values():
    print(items)
```
- Here is an exercise that shows printing the names with the bill amount for each person
```python
for value in food_bill.values():
    print(f"Name: {value['name']}\nBill: {value['bill']}\n")
```

### What are WHILE Loops ?
- The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
- We generally use this loop when we don't know the number of times to iterate beforehand.