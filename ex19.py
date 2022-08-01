#Define the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    '''A function that take number of cheese and number of crackers
    and uses them to make statments.'''
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket. \n")

#Here the arguments are straight up integer numbers
print("We can just give the function numbers directly")
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#Here the arguments are variables created for earlier
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Here the arguments are the results of simple math operations. 
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Here the assigned variables are used with math operations.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)