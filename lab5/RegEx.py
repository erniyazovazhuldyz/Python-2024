import re
def match_string(input_string):
    pattern = re.compile(r'a+b*')
    match = pattern.fullmatch(input_string)
    
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

match_string("ab")      
match_string("aab")      
match_string("abb")      
match_string("a")         
match_string("ac")        
match_string("bcd")       
match_string("abcde")  
#task1


import re
def match_string(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)
    
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

match_string("abb")
match_string("abbb")
match_string("abbbb")
match_string("ab")
match_string("ac")
match_string("abcde")
#task2


import re
def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

find_sequences("abc_def")
find_sequences("hello_world")
find_sequences("no_match_here")
find_sequences("a_b_c_d")
find_sequences("123_abc_456")
#task3


import re
def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

find_sequences("HelloWorld")
find_sequences("PythonProgramming")
find_sequences("NoMatchHere")
find_sequences("ABcDefG")
find_sequences("123abc456")
#task4


import re
def match_string(input_string):
    pattern = re.compile(r'a.*b$')
    match = pattern.fullmatch(input_string)
    
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

match_string("acdb")
match_string("abcdefb")
match_string("axbyczb")
match_string("ab")
match_string("abcde")
match_string("123ab456")
#task5


import re
def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]')
    replaced_string = pattern.sub(':', input_string)
    
    print(f'Original string: "{input_string}"')
    print(f'Replaced string: "{replaced_string}"')

replace_characters("Hello, World!")       
replace_characters("Python is fun.")   
replace_characters("This is a test.")     
replace_characters("NoReplacementNeeded") 
#task6


def snake_to_camel(snake_case_string):
    return ''.join(word.capitalize() for word in snake_case_string.split('_'))

snake_case_str = "hello_world_example"
camel_case_str = snake_to_camel(snake_case_str)
print(f'Snake Case: {snake_case_str}')
print(f'Camel Case: {camel_case_str}')
#task7


import re
def split_at_uppercase(input_string):
    result = re.findall('[a-zA-Z][^A-Z]*', input_string)
    return result

input_str = "HelloWorldExample"
result_list = split_at_uppercase(input_str)
print(f'Original String: {input_str}')
print(f'Split at Uppercase: {result_list}')
#task8


import re
def insert_spaces(input_string):
    spaced_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return spaced_string

input_str = "HelloWorldExample"
spaced_str = insert_spaces(input_str)
print(f'Original String: {input_str}')
print(f'With Spaces: {spaced_str}')
#task9


def camel_to_snake(camel_case_string):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case_string]).lstrip('_')

camel_case_str = "HelloWorldExample"
snake_case_str = camel_to_snake(camel_case_str)
print(f'Camel Case: {camel_case_str}')
print(f'Snake Case: {snake_case_str}')
#task10



