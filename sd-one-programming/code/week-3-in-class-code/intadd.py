#Author: Abdul Waajid 
#Date: 7th Oct 2024
#Write a program that converts user_input string values into
#integers and prforms basic arithmetic (sum, difference, product).

"""
Begin
ask input for number 
ask input for number two
convert the input numbers into integer

add the two numbers
find the difference between the two numbers
find the product of the two numbers

Output the results of the operations.

end 
"""

# code

n_one=int(input("Enter number one: "))
n_two=int(input('Enter number two: '))

tot = n_one+n_two
prod= n_one*n_two
diff = n_one-n_two

print(f"The total of {n_one} and {n_two} is {tot}\nThe product of {n_one} and {n_two} is \
        {prod}\nThe difference of {n_one} and {n_two} is {diff}")
# using \ allows the code to  be completed in the following line 
