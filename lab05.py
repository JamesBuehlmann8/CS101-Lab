########################################################################
##
## CS 101 Lab
## Program #5
## Name: James Buehlmann
## Email: jjbnp5@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Import String module
##      2. Define a function named get_school
##      3. Define a function named get_grade
##      4. Define a function named character_value
##      5. Define a function named get_check_digit
##      6. Define a function named verify_check_digit
##      7. When verify_chekc_digit is True program will display the school name and grade of student. 
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements
import string #Import string module

# functions
def get_school(student_id : str) -> str: #Creating function to determine which school the students library card is for
    if student_id[5] == '1':
        return 'School of Computing and Engineering SCE'#If index 5 of student's id is 1 than School of Computing and Engineering SCE is returned 
    elif student_id[5] == '2':
        return 'School of Law' #If index 5 of student's id is is 2 than School of Law is returned
    elif student_id[5] == '3':
        return 'College of Arts and Sciences' #If index 5 of student's id is 3 than College of Arts and Sciences is returned
    else:
        return 'Invalid School' #If index 5 of student's id is not 1,2,or 3 than error is returned

def get_grade(student_id : str) -> str: #Creating function to determine which grade the student is in based on thier student id
   if student_id[6] == '1':
       return 'Freshman' #If index 6 of student's id is 1 than Freshmen is returned
   elif student_id[6] == '2':
       return 'Sophomore' #If index 6 of student's id is 2 than Sophomore is returned
   elif student_id[6] == '3':
       return 'Junior' #If index 6 of studen's id is 3 than Junior is returned
   elif student_id[6] == '4':
       return 'Senior' #If index 6 of student's id is 4 than Senior is returned
   else:
       return 'Invalid Grade' #If index 6 of student's id is not 1,2,3,or 4 than error is returned

def character_value(ch : str) -> int: #Creating a function to convert letters to a numeric value
    return string.ascii_uppercase.index(ch) #Coverts A to 0, B to 1, .... Z to 25.

def get_check_digit(student_id : str) -> int: #Creating a function to return a check digit for the students ID
    total = 0
    for i in range(0,5):
        total += ((i + 1) * character_value(student_id[i])) #Multiplies (index +1) with (Character_Value of student Id) for first 5 characters
    for i in range(5,10):
        total += ((i + 1) *int(student_id[i])) #Multiplies (Index +1) with (integers of the remaing characters) and adds them to our current total
    return total % 10

def verify_check_digit(student_id : str) -> tuple: #Creating a function to verify our check digit
    if len(student_id) != 10:
        return False, 'The length of the number given must be 10.' #If the length of the student's id is not equal to 10 then return false
    elif student_id[0:5].isalpha() != True:
        for i in range(0,5):
            if student_id[i].isalpha() !=True:
                return False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}.'.format(i, student_id[i]) #If the first 5 characters are not letters than return false
    elif student_id[7:10].isdigit() != True:
        for i in range(7,10):
            if student_id[i].isdigit() !=True:
                return False, 'The last three characters must be 0-9, the invalid character is at {} is {}.'.format(i, student_id[i]) #If the last 3 characters are not numbers than return false
    elif student_id[5] != '1' and student_id[5] != '2' and student_id[5] != '3':
        return False, 'The sixth character must be 1 2 or 3.' #If the 6th character is not 1,2 or 3 than return false
    elif student_id[6] != '1' and student_id[6] != '2' and student_id[6] != '3' and student_id[6] != '4':
        return False, 'The seventh character must be 1 2 3 or 4.' #if the 7th character is not 1,2,3 or 4 return false
    elif int(student_id[9]) != get_check_digit(student_id): 
        return False, 'Check Digit {} does not match calculated value {}.'.format(student_id[9], get_check_digit(student_id)) #If last digit does not match check digit return false
    else:
        return True, '' #If all if statements are false than return true

if __name__ == "__main__": #Main Program
    print('                         Linda Hall')
    print('                     Library Card Check')
    print('============================================================')
    print() #Printing Header
    while True:
        print()
        library_card = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip() #Asking for student's library card id
        if library_card == "":
            break
        result, error = verify_check_digit(library_card) #If input is left blank break
       
        if result == True:
            print("Library card is valid.") #Prints if verify_check_digit is true
            print("The card belongs to a student in {}.".format(get_school(library_card))) #Prints the which school the library card belongs to
            print("The card belongs to a {}.".format(get_grade(library_card))) #Prints the grade of student the library card belongs to
        else:
            print("Libary card is invalid.") #Error statement
            print(error)
