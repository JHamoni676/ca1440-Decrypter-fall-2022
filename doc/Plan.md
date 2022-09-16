# Software Development Plan

# Phase 0: Requirements Specification

## **Deliver:**

The Duckie Decrypter is a program that converts DuckieCrypt to readable text.

*   The user is prompted to input the name of a file
    *   If the file is missing or cannot be opened, an error message will be displayed
    *   Or if the file contains only invalid DuckieCrypt
    *   If the input is good, the message will be displayed correctly decrypted

## Documentation For This Phase

### Things I already know how to do

*   I know how to read files in Pythong
*   I know how to split strings and read each individual character
*   I know how to convert strings to all lower or upper case

### Things I don't know how to do

*  

# Phase 1: System Analysis

## **Deliver:**

### Input

*   Data used by this program will be entered as a filepath to point to the file which will be used to decyrpt

### Output

*   Output will be:
    *   An error message for invalid file paths or unable to access the file
    *   No output will be printed if there is only invalid DuckieCrypt
    *   Correctly decrypted output if a file contains both all valid Duckiecrypt or a mixture of both valid and invalid crypt

### Algorithms

*   An algorithm to determine if the filepath is valid or the file is accessible
*   An algorithm that converts duckiecrypt to readable output
*   An algorithm that removes invalid input duckiecrypt


# Phase 2: Design *(30%)*


In the system analysis, it was decided that the program deal with three inputs

*   No input
*   Valid input
*   Invalid input


````
def converToLower(charCode):
    remove index[0] from charCode
    convert remaining string to int
    add 97 to the int
    pass into chr() = new string
    return new string

````

````
def convertToUpper(charCode):
    remove index[0] from charCode
    convert remaining string to int
    add 65 to the int
    pass into chr() = new string
    return new string
````

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

````
def decryptLine(line):
    initialize empty string output = ""
    loop through each index of the list line:
        output += decryptCharacter(line[i])
    return outpu
````

````
def getFile(pathToFile):
    checks if the filepath exists
    if it does exist:
        create a file object with open(filePath)
        returns opened file
    else:
        exits program
````


# Phase 3: Implementation *(15%)*

## **Deliver:**

*   (More or less) working Python code in `src/`.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
    *   If you have nothing of note in this section, **note that you had nothing to note here, do not leave it blank.**

## Documentation For This Phase


# Phase 4: Testing & Debugging *(30%)*

## **Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

## Documentation For This Phase


# Phase 5: Deployment *(5%)*

## **Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.

## Documentation For This Phase


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
