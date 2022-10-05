############################################################################## 
#                                                                            #                       
#   argparse — Parser for command-line options, arguments and sub-commands   #     
#                                                                            #
#   Ironhack Data Part Time --> Nov-2021                                     #
#                                                                            #
##############################################################################


# import library

import argparse


# Script functions 

def sum_function(x1, x2):
    return x1 + x2

def multiply_function(x1, x2):
    return x1 * x2


# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description='Set operation type')
    parser.add_argument("-f", "--function", help="function type. Options are: 'sum' and 'multiply'" , type=str) #"--function" ES UN ATRIBUTO QUE INVOCAMOS MAS ADELANTE
    args = parser.parse_args()
    return args


# Main pipeline function

def main(arguments):
    print('--//--- starting application ---//--')
    print('\n')
    n = float(input('Please, enter the first number:   '))
    m = float(input('Please, enter the second number:  '))
    if arguments.function == 'sum': #ATRIBUTO INVOCADO
        result = sum_function(n, m)
    elif arguments.function == 'multiply': #ATRIBUTO INVOCADO
        result = multiply_function(n, m)
    print('\n\n')
    print(f'The result is ==> {result}
    ')
    print('\n')
    print('--//--- closing application ---//--')


# Pipeline execution

if __name__ == '__main__':
    main(argument_parser())
