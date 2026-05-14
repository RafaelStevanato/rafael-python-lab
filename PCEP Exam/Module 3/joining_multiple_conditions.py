user_age = int(input("What is your age? "))
user_country = input("What is your country? ")
if user_age < 25 and user_country == "Germany":
    print ("You can apply for a German student exchange program.")
else:
    print ("Sorry, you do not qualify.")




user_country = input("What is your country? ")
if user_country == "Sweden" or user_country == "Norway" or user_country == "Denmark":
    print ("You can apply for a Scandinavian student exchange program.")
else:
    print ("Sorry, you do not qualify.")






user_country = input("Where do you come from? ")
if not user_country == "Germany":
    print("You are not from Germany.")
else:
    print("You are from Germany.")

