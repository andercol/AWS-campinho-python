
# 114- [PF] -Lab - Condicionais 

userReply = input("\nDo you need to ship a package? (Enter yes or no) \n")

if userReply =="yes":
    print("we can help you ship that package!\n")
else:
    print("Please come back when you need to ship a package. Thank you.\n")

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy)\n")
if userReply == "stamps":
    print("\nWe hva many stamp designs to choose from.\n")
elif userReply == "envelope":
    print("\nWe hava many envelope sizes to choose from.\n")
elif userReply == "copy":
    copies = input("\nHow many copies would you like? (Enter a number) ")
    print("\nHere are {} copies.".format(copies))
else:
    print("\nThank you, please come again.")