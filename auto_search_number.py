import random
number=random.randint(1,1000)
attempts=0
h=1000
l=1
while True:
    print('guess the correct number(between 1 to 1000):')
    input_number=(h+l)//2
    print('the guess number is:',input_number)
    attempts +=1
    if input_number == number:
        print('correct! your guess is right')
        break
    if input_number>number:
        print('incorrect! try a smaller number')
        h=input_number-1
    else:
        print('incorrect! try a  larger number')
        l=input_number+1
print('you tried',attempts,'times to find the correct number!')