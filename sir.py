import turtle

name=turtle.textinput('name','hello,what is your name?')
name=name.lower()

if name.startswith('mr'):
    print('Hello sir,what\'s up?')
elif  name.startswith('miss') or name.startswith('mrs'):
    print('Hello madam,How are you?')
else:
    name=name.capitalize()
    str='hi' +name+ '! how are you?'
    print(str)
turtle.exitonclick()
