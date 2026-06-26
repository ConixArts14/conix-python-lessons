age = 15

if age >= 13:
    print("You are a teenager.")
    if age >= 18:
        print("You are also an adult.")
    else:
        print("You are not yet an adult.")
else:
    print("You are a child.")

# Activity 1
print("\n=== Activity 1: Teenager and Test Score ===")
age = 14
score = 80
if age >= 13 and score >= 75:
    print("Teenager who passed!")

if age < 13 or score < 75:
    print("Either too young or failed.")

if not score < 75:
    print("Score is not less than 75.")
    
# Activity 2
print("\n=== Activity 2: Young and Low Score ===")
age = 10
score = 60

if age >= 13 and score >= 75:
    print("Teenager who passed!")

if age < 13 or score < 75:
    print("Either too young or failed.")

if not age < 13:
    print("Age is not less than 13.")

# Activity 3
print("\n=== Activity 3: Membership and Discount ===")
is_member = True
purchase_amount = 150
is_holiday = False

if is_member and purchase_amount > 100:
    print("You get a 10% discount!")

if is_holiday or (is_member and purchase_amount > 50):
    print("Special offer applies!")

if not is_member:
    print("Join our membership for benefits!")
else:
    print("Thanks for being a member!")
