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

## **Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

In the system analysis, it was decided that the program deal with three inputs

*   No input
*   Valid input
*   Invalid input

### Functions that deal with no input


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
