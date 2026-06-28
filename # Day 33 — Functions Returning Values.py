# Activity 1: Functions Returning Values
#def square(number):
    #return number * number

#result = square(5)
#print(f"The square of 5 is {result}.")


# Activity 2: Functions with Multiple Returning
#def check_number(number):
   # if number > 0:
        #return "positive"
    #elif number < 0:
        #return "Negative"
    #else:
        #return "Zero"
    
    #result1 = check_number(10)
    #result2 = check_number(-5)
    #result3 = check_number(0)

    #print(f"10 is {result}")
  #  print(f"-5 is {result2}")
   # print(f"0 is {result3}")


# Activity 3: Functions Returning Multiple Values
#def get_stats(a, b):
    #sum_result = a + b
    #product_result = a * b
    #return sum_result, product_result

#x, y = get_stats(4, 5)
#print(f"Sum: {x}, Product: {y}")

# Activity 4: Functions with Nested Returns
#def outer_function(a, b):
    #def inner_sum():
        #return a + b
    #def inner_product():
        #return a * b
    #return inner_sum(), inner_product()

#sum_result, product_result = outer_function(4, 6)
#print(f"Sum: {sum_result}, Product: {product_result}"


# Activity 5: Functions with Conditional Returns
def check_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

print(check_grade(95))   # Excellent
print(check_grade(80))   # Good
print(check_grade(55))   # Pass
print(check_grade(40))   # Fail


