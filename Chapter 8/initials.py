"""
The purpose of this program is to prompt the user for their full name.
Then display their first, middle, and last initials.
    ex. John William Smith should display J.W.S
"""
def main():
    Try_Again = "y"

    while Try_Again == "Y" or Try_Again == "y":
        #Get user input
        user_Input = input("Please enter your first middle and last name: ")
        
        #Split the string
        user_Name = user_Input.split()
       
        #Assign the split string variable names and identify first initials
        First_Name = user_Name[0]
        Middle_Name = user_Name[1]
        Last_Name = user_Name[2]

        #Print initials
        print(First_Name[0],".", Middle_Name[0],".", Last_Name[0])
        Try_Again = input("Would you like to enter another name? Type Y or N: y")

main()




