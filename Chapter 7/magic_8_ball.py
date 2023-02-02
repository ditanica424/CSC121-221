# Ditanica Farley     Lab 7-13     January 19, 2023

"""
This program should simulate a Magic 8 Ball. The program should read the 
responses from a file into a list. It should then prompt the user 
to input a "yes or no" question. The program should then generate a random 
number and select that item from the list and display the answer. 
The program should continue to prompt for questions until told toquit.
"""
import random

def main():
    #Create a variable to control the while loop
    Quit = "N"
    
    while Quit == "N" or Quit == "n":
    
        #Open the file named 8_ball_responses
        responses = open('8_ball_responses.txt', 'r')
    
        #Read the file's content into a list*
        file_contents = responses.readlines()
    
        #Close the file
        responses.close()
        
        #Open the file for reading
        infile = open("8_ball_responses.txt", "r")
        
        #read the contents of the file into a list
        responses= infile.readlines()
        
        #Close the file
        infile.close()
        
        #Strip the \n from each element
        index = 0
        while index < len(responses):
            responses[index] = responses[index].rstrip("\n")
            index += 1
        
        #Get user input*
        question = input("Please ask a yes of Yes or No question: ")
        
        #assign the random number to the the variable number*
        number = random_number()
        
        #print the response at the index location tha coresponds with the random number
        print(responses[number])
        print()
        
        #ask the use if they would like to quit*
        Quit = input("Would you like to quit? ")
        

#Generates the random number*    
def random_number():
    number = random.randint(0,11)
    
    return number
    
main()
