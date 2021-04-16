


"""
The program will determin which of teh two options is better.
The first option is 100 dollars per day for 10 days.
The second option is 1 dollar a day and it doubles each day for 10 days.
There will be to functions to calculate the pay rate.
Fuction1 will calculate the amount for the first option; function2 will calculate the amount for te second option.

fuction1 will output 100 * 10 days.
fuction2 will loop through 10 times, each time it will be doubling the amount and will add the amount to the total.

If the amount is equal, we output to th user "Option 1 and Option 2 pay the same"
If the option1 is better, we output to the user "Option 1 is better"
If the option2 is better, we output to the user "Option 2 is better"
"""


"""
# option1
    return 100 * 10
# option2
    amount = 1
    list1 = []
    loop 10 times
        add amount to list1
        amount *=2
        sum = sum of all items in loop
    return sum
# main
    var1 = option1
    var2 = option2

if var1 = var2
    "Option 1 and Option 2 pays the same"
if var1 < var2
    "Option 2 is better"
else
    "Option 1 is better"
main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0,10):
        list1.append(amount)
        amount *= 2
    print("list", list1)
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    elif var1 < var2:
        answer = "Option 2 is better"
    else:
        answer = "Option 1 is better"
    print(answer)

main()

