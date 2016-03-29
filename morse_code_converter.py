# morse_code_converter.py
# Exercise Selected: Chapter 11 program 9
# Name of program: Morse Code Converter
# Description of program:  This program takes a string of characters
#   input by the user and converts the string to morse code.  It then
#   displays the converted string to the user.


def main():
    # Local variables
    results = ''

    # Display the intro to the user.
    fluffy_intro()

    # todo: write the actual program

    # Display the results to the user.
    display_results(results)
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Morse Code Converter.')
    print('This program converts a string of characters into morse code'
          ' and displays the results.')
    return None


# Displays the summation results to the user.
def display_results(results):
    sep = '\n\n{}\n\n'.format('-'*79)
    print('{0}The morse code for your string is:\n{1} {0}'
          ''.format(sep, results))
    return None