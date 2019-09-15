def reversed(string):
    reversed_string= ' '
    for i in string:
        reversed_string = i+reversed_string
    print('reversed string is:', reversed_string)

string=input('enter string:')
print('entered string:',string)
reversed (string)
