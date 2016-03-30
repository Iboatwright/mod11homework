# morse_code_converter.py
# Exercise Selected: Chapter 11 program 9
# Name of program: Morse Code Converter
# Description of program:  This program takes a string of characters
#   input by the user and converts the string to Morse Code.  It then
#   displays the converted string to the user.


def main():
    # Local variables
    results = ''
    
    # Morse Code dictionary
    morse = {'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
             '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
             'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.',
             'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
             'm':'--','n':'-.','o':'---','p':'.---.','q':'--.-','r':'.-.',
             's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
             'y':'-.--','z':'--..',' ':' ',',':'--..--','.':'.-.-.-',
             '?':'..--..'}

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


# Returns a string used to identify a new part(i.e. page) of the program.
def page_header(title):
    return '{0:-<62}\n\n{1:^67}\n{0:_<62}\n'.format('    ', title)


# Displays the summation results to the user.
def display_results(results):
    sep = '\n\n{}\n\n'.format('-'*79)
    print('{0}The morse code for your string is:\n{1} {0}'
          ''.format(sep, results))
    return None