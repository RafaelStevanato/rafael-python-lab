user_age = int(input("What is yout age?"))

if user_age > 30:
    print("You are over 30 years old.")
    print("You do not qualify.")
elif user_age == 30:
    print("You are exactly 30 years old.")
    print("You will need to meet specific conditions to qualify!")  
else:
    print("You are below 30 years old.")
    print("Congratulations, you qualify!")