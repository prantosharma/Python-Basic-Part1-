import random

number=random.randint(1,20)
attempts=0
while True:
    input_number=input('guess the number(between 1 to 20):')
    input_number=int(input_number)
    attempts +=1
    if input_number==number:
        print('correct! your answer is true')
        break
    if input_number> number:
        print('incorrect!try to guess a smaller number')
    else:
        print('incorrect!try to guess a larger number')
print('you tried',attempts,'times to find the correct nunber')

