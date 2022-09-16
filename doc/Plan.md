# Software Development Plan

# Phase 0: Requirements Specification

## Documentation

The Duckie Decrypter is a program that converts DuckieCrypt to readable text.

*   The user is prompted to input the name of a file
    *   If the file is missing or cannot be opened, an error message will be displayed
    *   Or if the file contains only invalid DuckieCrypt
    *   If the input is good, the message will be displayed correctly decrypted


### Things I already know how to do

*   I know how to read files in Python
*   I know how to split strings and read each individual character
*   I know how to convert strings to all lower or upper case
*   I know how to use if statements as validation
*   I know how to slice strings

### Things I don't know how to do

*   I did not remember how to slice strings correctly to begin with

# Phase 1: System Analysis

## **Deliver:**

### Input

*   Data used by this program will be entered as a filepath to point to the file which will be used to decyrpt

### Output

*   Output will be:
    *   An error message for invalid file paths or unable to access the file
    *   No output will be printed if there is only invalid duckie crypt
    *   Correctly decrypted output if a file contains both all valid duckie crypt or a mixture of both valid and invalid crypt

### Algorithms

*   An algorithm to determine if the filepath is valid or the file is accessible
*   An algorithm that converts duckie crypt to readable output
*   An algorithm that converts invaldi duckie crypt to empty strings


# Phase 2: Design


In the system analysis, it was decided that the program deal with three inputs

*   Valid input
*   Invalid input

### Converts duckie crypt with the "_" tag to lowercase letters
*   Takes a duckie crypt character code as a string
*   Returns a readable string
````
def converToLower(charCode):
    remove index[0] from charCode
    convert remaining string to int
    add 97 to the int
    pass into chr() = new string
    return new string

````
### Converts duckie crypt with the "^" tag to uppercase letters
*   Takes a duckie crypt character code as a string
*   Returns a readable string
````
def convertToUpper(charCode):
    remove index[0] from charCode
    convert remaining string to int
    add 65 to the int
    pass into chr() = new string
    return new string
````
### Converts duckie crypt with the "+" tag to special characters
*   Takes a duckie crypt character code as a string
*   Returns a readable string
````
def convertToSpecialChar(charCode):
    checks if character is valid duckieCrypt
    remove index [0] from the character code string
        #Algorithm to return decrypted string
    if the ord(initial character) = 65 then group A:
        remove the grouping character
        convert remaining string to int
        add 32 to the int
        pass into chr() = new string
        return new string
    if ord(initial character) = 66 then group B:
        remove grouping character
        convert remaining string to int
        add 91 to int
        pass into chr() = new string
        return new string
    if ord(initial character) = 76 then group C:
        remove grouping character
        convert remaining to int
        add 123 to int
        pass into chr() = new string
        retrun new string
    else:
        return "" 
````
### Separates duckie crypt character codes into different categories
*   Takes a duckie crypt character code as a string
*   Categorizes the character code into:
  *   Uppercase letters
  *   Lowercase letters
  *   Special characters
*   Returns the character code being passed into the appropriate converter:
  *   convertToUpper()
  *   convertToLower()
  *   convertToSpecialChar()
````
def decryptCharacter(character):
    for loop to split character to know whether to feed to
    convert initial character to int value using ord(character[0]) = charValue
    if charValue = 43:
        return convertToSpecialChar(character)
    if charValue = 94:
        return convertToUpper(character)
    if charValue = 95:
        return convertToLower(character)
    else:
        return ""
````
### Splits a large string into a list of character codes
````
def decryptLine(line):
    initialize empty string output = ""
    loop through each index of the list line:
        output += decryptCharacter(line[i])
    return outpu
````
### Validates path files and opens the file if valid
````
def getFile(pathToFile):
    checks if the filepath exists
    if it does exist:
        create a file object with open(filePath)
        returns opened file
    else:
        exits program
````


# Phase 3: Implementation

## Documentation For This Phase

*   Refer to working code in ../src/duckieDecrypter.py


# Phase 4: Testing & Debugging

## **Documentation For This Phase:**

After finishing the program the decoder was failing when passing in invalid0.txt. After adding validation I was using the & symbol instead of
"and" in the validation if statements.

When testing with ../data/testing/invalid1.txt I found that I did not have validation for the special characters to make
make sure the ascii code stays within the valid duckie crypt bounds.

When testing with ../data/testing/invalid2.txt I found that the program did not handle a character code
that did not have a number at the end of a special character identification code


# Phase 5: Deployment

## **Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
      *   COMPLETED
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.
      *   COMPLETED



# Phase 6: Maintenance

## **Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
        *   the operating system?
        *   to the next version of Python?

## Documentation For This Phase

*   The part I am no the happiest about is the convertToSpecialChar() method. I kind of wish I had created a separate method to put to sorting logic in
*   I know how all of the program works
*   It would probably take me 20 min to find and fix a bug in a few months
*   I believe the documentation will make sense to most people, but it could be confusing
*   I would remember it and understand the documentation
*   It would probably be a little more then a minor issue to add a feature in a year
*   I believe that it would keep working, but maybe not 3 or 4 versions of python from now