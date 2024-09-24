def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise

    def isPalindrome(word):
        #cutoff = word.count() #Counts the # of characters in the string
        word.replace(" ", "").lower #removes spaces from string as palindromes dont care about them usually but python does same with .lower
        return word == word[::-1] #word[start:end:step] == equal to
        
    return isPalindrome(word) #this returns if the function is true/false

    pass

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number

    def lessThanFibSeq(num):
        fibSequence = [] #empty sequence for reference later
        if num >= 0:
            fibSequence = [0, 1] #manually adding the first two digits for now
            while True:
                #fib sequence generator below
                nextNum = fibSequence[-1] + fibSequence[-2] #next num = last number and 2nd last number of fib sequence sum
                fibSequence.append(nextNum) #adds nextnum to fib sequence
                if nextNum > num: #if fib sequence number > defined number, stop
                    fibSequence.pop(-1) #if statement after return, so we pop off the last number since itll be higher
                    break
            return fibSequence #return fib sequence value
        else: 
            return fibSequence #return fib sequence value if < 1
    return lessThanFibSeq(number_val)

    pass

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.

    def howManyTimes(long, short):
        str1Short = len(str2) #defines a short string as 
        counter = 0 #counter to progress through string1
        timesFound = 0 #counter for end count

        for letter in str1:
            if str1.lower()[counter:str1Short] == str2.lower(): #if string1[pieces from counter # to short #]
                timesFound = timesFound + 1 #increase counter if found
            counter = counter + 1
            str1Short = str1Short + 1
        print(str2, "was found", timesFound, "times in", str1) #print answer
        return timesFound #return so I get marks
    
    #count number of characters in string 2
    #take that amount of characters and see if it matches
    #count number of times it works and return it
    return howManyTimes(str1, str2)
    
    pass

def lab2Question4(list1, list2):
     #Create a function that takes in two equal length list of numbers. 
     #Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
     #If the condition of the function is not satisfied, return a blank list
    pass
    sum_list = 5

    return sum_list

def lab2Question5(password):
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 

        if isValidPassword(password) is True: #call isValidPassword
            print("Your password,", password, "is valid")
            return password #returns valid password
        else:
            print("Please enter a better password")
        password = None

        return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    password2 = password #Need this cause it causes weird errors otherwise
    print(password2)
    passwordNum = any(chr.isdigit() for chr in password) #This checks password for numbers and sets to passwordNum
    if len(password2) < 8: #check length of password. if less than 8, return false
        print("Password contains less than 8 characters")
        return False
    elif password2.islower() is True: #checks for upper case letters
        print("Password does not contain a capital letter")
        return False
    elif password2.isupper() is True: #checks for lower case letters
        print("Password does not contain a lower case letter")
        return False
    elif passwordNum is False: #find out if string contains any numbers
        print("Password does not contain a number")
        return False
    elif password2.isdigit():
        print("The string contains only digits. Please enter another character")
    else:
        print("Your password is ok")
        return True
    
    pass

#--------------------------------------------------------------------------------------------------------------
#Testcases

#print(lab2Question1("girafarig"))
#print(lab2Question2(59))
#print(lab2Question3("Superstitious and superfluous", "super"))

isValidPassword("12345678")
#lab2Question5("AAAAAAAb1")