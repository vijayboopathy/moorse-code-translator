"""
1. Take input from the user
2. Compare input against dictionary
3. Print output
"""
morse_dict = { 'A':'.-', 'B':'-...',
               'C':'-.-.', 'D':'-..', 'E':'.',
               'F':'..-.', 'G':'--.', 'H':'....',
               'I':'..', 'J':'.---', 'K':'-.-',
               'L':'.-..', 'M':'--', 'N':'-.',
               'O':'---', 'P':'.--.', 'Q':'--.-',
               'R':'.-.', 'S':'...', 'T':'-',
               'U':'..-', 'V':'...-', 'W':'.--',
               'X':'-..-', 'Y':'-.--', 'Z':'--..',
               '1':'.----', '2':'..---', '3':'...--',
               '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.',
               '0':'-----', ', ':'--..--', '.':'.-.-.-',
               '?':'..--..', '/':'-..-.', '-':'-....-',
               '(':'-.--.', ')':'-.--.-'}

def parse_input(input_morse):
  split_input = input_morse.split()
  return split_input

def match_input(input_morse):
  parsed_input = parse_input(input_morse)
  result = ''
  for i in parsed_input:
    op_set = {k for (k,v) in morse_dict.items() if i==v}
    result += ''.join(op_set)
  return result

def convert_input(input_string):
  uppercase_input = input_string.upper()
  input_list = uppercase_input.replace(' ', '')
  result = ''
  for i in input_list:
    op_list = [v for (k,v) in morse_dict.items() if k==i]
    result += ' '
    result += ' '.join(op_list) # space in join doesn't work for list of lists
  return result

input_morse = '... --- ...'
input_string = 'Vijayboopathy Elangovan'
print(match_input(input_morse))
print(convert_input(input_string))
