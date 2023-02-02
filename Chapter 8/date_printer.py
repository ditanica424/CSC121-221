
def main():
    #**INPUT**
    #Get user input
    user_Input = input("Please enter a date in the format: mm/dd/yyyy: ")

    #**PROCESSING**
    #Split String
    date_String = user_Input.split("/")

    #Assign date_String value at index 0 to the variable Month
    Month = date_String[0]

    #Convert the numberic string to alphabetic string
    if Month == "01":
        Month ="January"
    elif Month == "02":
        Month = "February"
    elif Month == "03":
        Month = "March"
    elif Month == "04":
        Month = "April"
    elif Month == "05":
        Month = "May"
    elif Month == "06":
        Month = "June"
    elif Month == "07":
        Month = "July"
    elif Month == "08":
        Month = "August"
    elif Month == "09":
        Month = "September"
    elif Month == "10":
        Month = "October"    
    elif Month == "11":
        Month = "November"  
    elif Month == "12":
        Month = "December"

    #Assign date_String value at index 1 to the variable Month
    Date = date_String[1]

    #Assign date_String value at index 2 to the variable Month
    Year = date_String[2]

    #**OUTPUT**
    print(Month, Date+",",Year)
main()