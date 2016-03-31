# morse_code_converter.py
# Exercise Selected: Chapter 11 program 9
# Name of program: Morse code Converter
# Description of program:  This program takes a string of characters
#   input by the user and converts the string to Morse code.  It then
#   displays the converted string to the user.


def main():
    # Local variables
    results = ''
    in_string = ''
    end_program = 'no'
    
    # Morse code dictionary
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

    # Control loop for the program.  The user answers yes to exit when
    #    prompted.
    while end_program.lower() in ['no','n','']:
        print(page_header('Morse Code Converter'))
        valid_out = []

        # This gets the user's input string.  It is not validated.
        in_string = get_in_string()

        # Discards any invalid characters in the input string, converts it
        #   into Morse code, then stores/returns it in the valid_out list.
        valid_out = convert_to_morse(in_string, morse)

        # Generates a print-friendly string from the Morse code list.
        results = prep_results(valid_out)

        # Display the results to the user.
        display_results(results)

        # Prompts the user if they want to exit and assigns the valid answer
        #   to the loop control variable.
        end_program = go_again()

    # Exit message.
    print('{:^80}'.format(prep_results(convert_to_morse('goodbye', morse),
                                       False)))
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print(page_header('Morse Code Converter'))
    print('Welcome to the Morse code Converter.')
    print('This program converts a string of characters into Morse code\n'
          ' and displays the results.  The chart below shows the valid\n'
          'characters and their Morse code. Characters not in this chart\n'
          'will be discarded.')
    print('''
        Morse Code Characters
        ---------------------
        space   space       6 -....     G --.       Q --.-
        comma   --..--      7 --...     H ....      R .-.
        period  .-.-.-      8 ---..     I ..        S ...
        ?       ..--..      9 ----.     J .---      T -
        0       -----       A .-        K -.-       U ..-
        1       .----       B -...      L .-..      V ...-
        2       ..---       C -.-.      M --        W .--
        3       ...--       D -..       N -.        X -..-
        4       ....-       E .         O ---       Y -.--
        5       .....       F ..-.      P .---.     Z --..
    ''')
    return None


# Returns a string used to identify a new part(i.e. page) of the program.
def page_header(title):
    return '{0:-<62}\n{1:^67}\n{0:_<62}\n'.format('    ', title)


# Asks the user to input a string of characters to be translated into
#   Morse code.
def get_in_string():
    prompt = 'Please enter a string of characters to be converted:\n\n'
    return input(prompt).lower()


# Convert the in_string into a string of Morse code and return to the
#      calling module.
def convert_to_morse(in_string, morse):
    valids = []
    valid_out=[]

    # Create a list from the in_string only using the characters used as
    #   keys in the morse dict.
    valids = [c for c in list(in_string) if c in morse.keys()]

    # Create a new list of values from the morse dict using each entry in
    #   the valids list as the key.
    valid_out = [morse[c] for c in valids]
    return valid_out


#  Format the Morse code string for ease of readability.  Each entry in the
#       valid_out list is concatenated with a trailing space in a temporary
#       string.  When the temp string is 70 or more characters long the
#       trailing whitespace is stripped and a newline is added.  The temp
#       string is set to '' after it's contents are appended to results.
def prep_results(valid_out, pre=True):
    results = ''
    tmp_res = ''
    pre_res = 'This is your message in Morse code:\n\n    '

    for m in valid_out:
        tmp_res += '{} '.format(m)
        if len(tmp_res) >= 70:
            results += '{}\n    '.format(tmp_res.rstrip())
            tmp_res = ''
    # After all characters are converted from valid_out any trailing
    #   characters in tmp_res are appended to results.
    if len(tmp_res) < 70:
        results += '{}\n    '.format(tmp_res.rstrip())
        tmp_res = ''
    # If the pre argument is set to False nothing is prepended to results.
    results = '{}{}'.format(pre_res, results) if pre else results
    return results


# Program loop control variable with validation.
def go_again():
    end_program = input('Do you want to exit the program? yes or (n)o\n >>> ')
    while end_program not in ['yes','y','no','n','']:
        end_program = input('Error: Invalid entry.  Type yes or no.')
    return end_program


# Displays the conversion results to the user.
def display_results(results):
    sep = '\n\n{}\n\n'.format('-'*79)
    print('{0}{1}{0}'
          ''.format(sep, results))
    return None


# Call main.
main()
