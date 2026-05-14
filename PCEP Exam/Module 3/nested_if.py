answer_a = input("Do you like traveling? y/n: ")

if answer_a == "y":
    print ("Good!")
    answer_b = input("And do you like Asia? y/n: ")
    if answer_b == "y":
        print ("Nice! You can take a ticket to Asia.")
    else:
        print ("That's sad to hear.")
else:
    print ("That's sad to hear.")