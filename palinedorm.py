def reverse(s):
    return s[::-1]

def praindom(s):
    rev = reverse(s)
    if (s==rev):
        print('this is palindrome')
    else:
        print('this is not palindrome')
s=input('type your string: ')
