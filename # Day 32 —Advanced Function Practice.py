# Activity 1: Function with Default Parameters
#def greet(name="Conix"):
    #print("Hello,", name, "! Welcome back to Day 32.")

#greet()
#greet("Leonald")

# Activity 2: Functions Returning Multiple Values
#def calculate(a, b):
    #sum_result = a + b
    #product_result = a * b
    #return sum_result, product_result

#sum_val, product_val = calculate(5, 3)
#print("Sum:", sum_val)
#print("Product:", product_val)

# Activity 3: Functions with Keyword Arguments
#def introduce(name, age, hobby):
    #print("My name is", name)
   # print("I am", age, "years old")
    #print("My hobby is", hobby)

#introduce("Conix", 10, "Programming")
#introduce(age=10, hobby="Programming", name="Conix")

# Activity 4: Nested Functions
#def outer_function(message):
   # def inner_function():
        #print("Inner says:", message)
    #inner_function()

#outer_function("Hello from Day 32!")



# Activity 5: Functions with Conditional Logic
def check_even_odd(number):
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")

check_even_odd(10)
check_even_odd(7)
