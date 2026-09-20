print("SU")
varname = input("question")

"""
a multiline comment

"""

print("hELLO" + varname)
# can use comma instead of +
# comma needs no type conversion and adds space in bw
# print(*objects, sep=' ', end="\n", file=sys.stdout, flush=False) the default python print syntax
# here we can change vals of anything watch changing end now
print("sanal", end="19")
#using seperator for print
print("sanal", "kumar", sep="*")#sep is used to change the default space in bw the objects
#print can be used with single or double quotes
#statements inside print can be put inside backslash to avoid syntax error
print("sanal's laptop")
print('sanal"s laptop')
print("sanal\"s laptop")#using backslash to avoid syntax error      
#using format string to print
name = "sanal"
age = 19
print("my name is {} and my age is {}".format(name, age))
#using f string to print
print(f"my name is {name} and my age is {age}")# from the video 
#using strip to remove extra spaces
name = "   sanal   "
print(name.strip())#strip removes extra spaces from both sides
print(name.lstrip())#lstrip removes extra spaces from left side
print(name.rstrip())#rstrip removes extra spaces from right side   
#you can also assign stripped value to a new variable
name = name.strip()
print(name)
#using title to capitalize first letter of each word
name = "sanal kumar"
print(name.title())#title capitalizes first letter of each word
#using upper to convert to uppercase
print(name.upper())#upper converts to uppercase
#using lower to convert to lowercase                
print(name.lower())#lower converts to lowercase     
#using capitalize to capitalize first letter of the string
print(name.capitalize())#capitalize capitalizes first letter of the string
#using all the functions together by assigning to a new variable

name = name.strip().title().upper()
print(name) 
#using all these with input function
name = input("enter your name: ").strip().title()
print(f"hello {name}")      
#using split to split a name into first and last name
name = "sanal kumar"
first_name, last_name = name.split()#split splits the string into a list of words
print(first_name)
print(last_name)        
#interactive code can be used in the terminal
#adding numbers using int type conversion
num1 = input("enter first number: ")
num2 = input("enter second number: ")
sum = int(num1) + int(num2)
print(f"the sum of {num1} and {num2} is {sum}") 
#same using changing the input type to int
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = num1 + num2      
print(f"the sum of {num1} and {num2} is {sum}")
#adding two numbers using print only in one line    
print(int(input("enter first number: ")) + int(input("enter second number: ")))
#syntax for float type conversion is float(input("enter a number: "))
#syntax for round function is round(number, ndigits) where number is the number to be rounded and ndigits is the number of decimal places to round to
num = float(input("enter a number: "))
rounded_num = round(num, 2)
print(f"the rounded number is {rounded_num}")   
#if no parameter is given to round function it rounds to the nearest integer
#using f string to introduce comma in a large number
num = 1000000
print(f"{num:,}")#using comma as a thousand separator   
#rounding floating digits using f string
num = 3.141592653589793
print(f"{num:.2f}")#using f string to round to 2 decimal places
#defining a function to print a greeting message
def greet(name):
    print(f"hello {name}, welcome to python programming!")
greet("sanal")  
#same function with default name as World
def greet(name="World"):
    print(f"hello {name}, welcome to python programming!")
greet()#using default name      
#same function defined using main function and greet function
def main():     
    name = input("enter your name: ")
    greet(name)
def greet(name):
    print(f"hello {name}, welcome to python programming!")
if __name__ == "__main__": #confused about this line
    main()
#to calculate square of a number using function
def square(num):
    return num * num
print(square(5))#using the function to calculate square of 5    
#to calculate square of a number using main function and square function    
def main():     
    num = int(input("enter a number: "))
    print(f"the square of {num} is {square(num)}")
def square(num):
    return num * num
if __name__ == "__main__":
    main()

#do the same using pow function
def main():     
    num = int(input("enter a number: "))
    print(f"the square of {num} is {pow(num, 2)}")          


if __name__ == "__main__":
    main()  
#do the same usign ** operator
def main():     
    num = int(input("enter a number: "))
    print(f"the square of {num} is {num ** 2}")     
if __name__ == "__main__":
    main()  

#use of if function to print largest of two numbers
def main(): 
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("both numbers are equal") 
if __name__ == "__main__":
    main()  
#example of using if with two or more conditions
def main(): 
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest number")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest number")
    elif num3 > num1 and num3 > num2:
        print(f"{num3} is the greatest number")
    else:
        print("all numbers are equal")
if __name__ == "__main__":
    main()  
#we can also use or instead of and in the above code to check if any two numbers are equal and greater than the third number
def main():         
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))
    if num1 > num2 or num1 > num3:
        print(f"{num1} is greater than {num2} or {num3}")
    elif num2 > num1 or num2 > num3:
        print(f"{num2} is greater than {num1} or {num3}")
    elif num3 > num1 or num3 > num2:
        print(f"{num3} is greater than {num1} or {num2}")
    else:
        print("all numbers are equal")          

if __name__ == "__main__":                                  
    main()  
#using if and else in one line
def main(): 
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print(f"{num1} is greater than {num2}" if num1 > num2 else f"{num2} is greater than {num1}")
if __name__ == "__main__":
    main()          
#parity checker using n%2==0 as the boolean return type of a function used to do the operation
def is_even(num):
    return num % 2 == 0
def main():
    num = int(input("enter a number: "))
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
if __name__ == "__main__":
    main()  
#using match case to check the day of the week
def main(): 
    day = input("enter a day of the week: ")
    match day.lower():
        case "monday":
            print("today is monday")
        case "tuesday":
            print("today is tuesday")
        case "wednesday":
            print("today is wednesday")
        case "thursday":
            print("today is thursday")
        case "friday":
            print("today is friday")
        case "saturday":
            print("today is saturday")
        case "sunday":
            print("today is sunday")
        case _:
            print("invalid day of the week")    
if __name__ == "__main__":
    main()      
# a case in which match is used to check multiple conditions in one case
def main(): 
    day = input("enter a day of the week: ")
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("today is a weekday")
        case "saturday" | "sunday":
            print("today is a weekend")
        case _:
            print("invalid day of the week")        

if __name__ == "__main__":
    main()      

#example for while loop
def main():
    num = int(input("enter a number: "))
    while num > 0:
        print(num)
        num -= 1        

if __name__ == "__main__":      
    main()  
#example for for loop
def main():     
    for i in range(1, 11):
        print(i)    
if __name__ == "__main__":
    main()      
#its output is 1 to 10 because range function generates a sequence of numbers from the start value (inclusive) to the end value (exclusive) and in this case it starts from 1 and ends at 11 (exclusive) so it generates numbers from 1 to 10.
#same using three numbers in sqaure brackets

def main():     
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(i)                            
if __name__ == "__main__":      
    main()  
#print a text three times using multiplication operator
def main():     
    text = "hello "
    print(text * 3)                     
if __name__ == "__main__":    
    main()

#making user give positive number only using while and boolean variable
def main():     
    num = int(input("enter a positive number: "))
    while num <= 0:
        print("please enter a positive number")
        num = int(input("enter a positive number: "))
    print(f"you entered {num}")
if __name__ == "__main__":    
    main()  
#another one in which while starts with while true and breaks when the condition is met
def main():    
    while True:
        num = int(input("enter a positive number: "))
        if num > 0:
            print(f"you entered {num}")
            break
        else:
            print("please enter a positive number")     

if __name__ == "__main__":    
    main()  

#print num number of meows from above code using for loop with _ as the variable name
def main():    
    num = int(input("enter a number: "))
    for _ in range(num):
        print("meow")
if __name__ == "__main__":    
    main()          

#_as variable name is used when we don't need to use the variable in the loop and we just want to repeat the loop a certain number of times. It is a convention to use _ as a variable name when we don't need to use it in the loop.   
#using lists and using for loop to print the elements of a list
def main():    
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    for fruit in fruits:
        print(fruit)#prints upto any number of fruits in the list as we are using for loop to iterate through the list and print each element of the list.
if __name__ == "__main__":    
    main() 
#use for with range in which range gets the length of the list and we can use the index to print the elements of the list
def main():    
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    for i in range(len(fruits)):
        print(fruits[i])#prints upto any number of fruits in the list as we are using for loop to iterate through the list and print each element of the list using the index.          
if __name__ == "__main__":    
    main()  
#using dict to and print the keys and values of a dict using for loop
def main():   
    person = {"name": "sanal", "age": 19, "city": "kochi"}
    for key in person:
        print(f"{key}: {person[key]}")#prints the keys and values of the dict using for loop to iterate through the dict and print each key and its corresponding value.
if __name__ == "__main__":
    main()  
#using none to represent the absence of a value in the above code we can use none to represent the absence of a value for a key in the dict and we can check if the value is none using an if statement
def main():    
    person = {"name": "sanal", "age": 19, "city": None}
    for key in person:
        if person[key] is None:
            print(f"{key}: value is not available")
        else:
            print(f"{key}: {person[key]}")#prints the keys and values of the dict using for loop to iterate through the dict and print each key and its corresponding value. If the value is none it prints that the value is not available.
if __name__ == "__main__":
    main()              
#using for loops with i and j to print a multiplication table
def main():    
    num = int(input("enter a number: "))
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{num} x {i} x {j} = {num * i * j}")#prints the multiplication table of the given number using nested for loops to iterate through the numbers from 1 to 10 and print the multiplication of the given number with each of those numbers.
if __name__ == "__main__":
    main()  
#evaluating string input for a integer input using try and except
def main():    
    try:
        num = int(input("enter a number: "))
        print(f"you entered {num}")
    except ValueError:
        print("please enter a valid integer")
if __name__ == "__main__":
    main()      
#here ValueError is case when the user enters a string instead of an integer and we can catch that error using except and print a message to the user to enter a valid integer. We can also catch other types of errors using different except blocks.  
#example of catching with except and else block
def main():                                                         
    try:
        num = int(input("enter a number: "))
    except ValueError:
        print("please enter a valid integer")
    else:
        print(f"you entered {num}")#prints the number entered by the user if it is a valid integer and if it is not a valid integer it catches the error and prints a message to the user to enter a valid integer. The else block is executed only if there is no error in the try block.
if __name__ == "__main__":  
    main() 
#returning a value from a function and catching the error in the main function
def get_number():    
    try:
        num = int(input("enter a number: "))
        return num
    except ValueError:
        print("please enter a valid integer")
        return None     
def main():   
    num = get_number()
    if num is not None:
        print(f"you entered {num}")
    
if __name__ == "__main__":
    main()  
#do the same without assigning the return value to a variable in the main function
def get_number():    
    try:
return int(input("enter a number: "))
    except ValueError:
        print("please enter a valid integer")
        return None             
def main():   
    if (num := get_number()) is not None:
        print(f"you entered {num}")     
if __name__ == "__main__":  
    main()
#use try with return only in the function and catch the error in the main function
def get_number():       
    try:
        return int(input("enter a number: "))
    except ValueError:
        print("please enter a valid integer")
        return None
def main():    
    num = get_number()
    if num is not None:
        print(f"you entered {num}")
if __name__ == "__main__":          
    main()  
#use pass instead of error message in the except block to ignore the error and return none
def get_number():    
    try:
        return int(input("enter a number: "))
    except ValueError:
        pass
    return None
def main():   
    num = get_number()
    if num is not None:
        print(f"you entered {num}")     
if __name__ == "__main__":    main()
#using raise to raise an error if the user enters a negative number
def get_positive_number():    
    num = int(input("enter a positive number: "))
    if num < 0:
        raise ValueError("please enter a positive number")
    return num
def main():    
    try:
        num = get_positive_number()
        print(f"you entered {num}")
    except ValueError as e: #THE USE of e is to catch the error message raised by the raise statement in the get_positive_number function and print it to the user. The variable e is used to store the error message and we can print it using print(e) in the except block. This way we can provide a more specific error message to the user when they enter a negative number.
        print(e)
if __name__ == "__main__":  main()  
#coin flip using random.choice to randomly select heads or tails
import random
def coin_flip():    
    return random.choice(["heads", "tails"])
def main():    
    result = coin_flip()
    print(f"you flipped {result}")
if __name__ == "__main__":    main()  
#avoid using random.choiche just use choice from random module to avoid writing random.choice every time
from random import choice
def coin_flip():                                        
    return choice(["heads", "tails"])                           
def main():                 



    result = coin_flip()
    print(f"you flipped {result}")
if __name__ == "__main__":      
    main()  
 #to print random number between 1 and 100 using random.randint function
from random import randint
def random_number():    
    return randint(1, 100)      
def main():     
    num = random_number()
    print(f"your random number is {num}")       
if __name__ == "__main__":    main()    
#shuffle a list of numbers using random.shuffle function
from random import shuffle  
def shuffle_list(lst):    
    shuffle(lst)
    return lst
def main():    
    numbers = [1, 2, 3, 4, 5]
    shuffled_numbers = shuffle_list(numbers)
    print(f"shuffled numbers: {shuffled_numbers}")
if __name__ == "__main__":    main()    
#example of mean in statistics module to calculate the mean of a list of numbers
from statistics import mean         
def calculate_mean(numbers):    
    return mean(numbers)
def main():    
    nums = [1, 2, 3, 4, 5]
    mean_value = calculate_mean(nums)
    print(f"the mean of {nums} is {mean_value}")
if __name__ == "__main__":    main()    
#using sysargv to print my name and age from command line arguments
import sys
def main():   
    if len(sys.argv) != 3:
        print("please provide your name and age as command line arguments")
        return
    name = sys.argv[1]
    age = sys.argv[2]
    print(f"hello {name}, you are {age} years old")     
if __name__ == "__main__":    main()
#here sysargv 0 is the name of the program and sysargv 1 and 2 are the name and age provided by the user as command line arguments. We check if the length of sysargv is not equal to 3 to ensure that the user has provided both name and age as command line arguments. If the length is not 3 we print a message to the user to provide the required arguments and return from the function. If the length is 3 we assign the name and age from sysargv and print a greeting message to the user with their name and age.        
#using try and except to catch the error if the user does not provide the required command line arguments
import sys
def main():  
    try:
        name = sys.argv[1]
        age = sys.argv[2]
        print(f"hello {name}, you are {age} years old")     
    except IndexError:
        print("please provide your name and age as command line arguments") 
if __name__ == "__main__":    main()
#you can put the command line arguements in double quotes if they contain spaces to avoid syntax error and to ensure that the arguments are treated as a single argument. For example, if your name is "sanal kumar" you can provide it as a command line argument like this: python hello.py "sanal kumar" 19. This way the name will be treated as a single argument and there will be no syntax error.   
#example of using for arg in argv to print all the command line arguments provided by the user
import sys
def main():   
    if len(sys.argv) < 2:
        print("please provide some command line arguments")
        return          
    for arg in sys.argv[1:]: #this line avoids the program name which is sys.argv[0] and starts the loop from sys.argv[1] to print only the command line arguments provided by the user.
        print(arg)
if __name__ == "__main__":    main()        
#here using return in the main function to exit the function if the user does not provide any command line arguments and using for loop to iterate through the command line arguments provided by the user and print each argument on a new line. We start the loop from sys.argv[1] to skip the name of the program which is sys.argv[0].  
#example of sysexit to exit the program if the user does not provide any command line arguments
import sys
def main():   
    if len(sys.argv) < 2:
        print("please provide some command line arguments")
        sys.exit()          
    for arg in sys.argv[1:]:
        print(arg)      
if __name__ == "__main__":    main()
#print a range of command line arguements provided by the user using slicing
import sys
def main():  
    if len(sys.argv) < 2:
        print("please provide some command line arguments")
        return          
    for arg in sys.argv[1:4]: #this line will print the first three command line arguments provided by the user starting from sys.argv[1] to sys.argv[3] and it will not print sys.argv[4] and onwards.
        print(arg)  
if __name__ == "__main__":    main()    
#using negative indexing to print the given command line arguemnts in reverse order
import sys
def main():   
    if len(sys.argv) < 2:
        print("please provide some command line arguments")
        return          
    for arg in sys.argv[-1:-4:-1]: #this line will print the last three command line arguments provided by the user in reverse order starting from sys.argv[-1] to sys.argv[-3] and it will not print sys.argv[-4] and onwards.
        print(arg)  
if __name__ == "__main__":    main()
#sequence[start:stop:step] is the syntax for slicing a sequence in python where start is the index to start the slice, stop is the index to end the slice and step is the number of indices to skip in the slice. In the above code we are using negative indexing to print the command line arguments in reverse order by starting from the last argument which is sys.argv[-1] and ending at sys.argv[-4] and skipping one index in each step to print only three arguments in reverse order. 
#here giving -1 in the step parameter to print the arguments in reverse order and giving -4 in the stop parameter to ensure that we only print three arguments in reverse order and not all the arguments in reverse order. If we give -1 in the stop parameter it will print all the arguments in reverse order which is not what we want. 
