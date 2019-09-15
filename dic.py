marks={1:10,2:20,3:30,5:50,6:60,4:40}
print('marks of roll number 4 is:',marks[4])

list_order={'pranto':102,'anik':103,'sabbir':104}
print('the serial no of applicant is:',list_order['pranto'])



dt={}
dt[1]='one'
print(type(dt))
print(dt)

#write a dictionary which store xm results and the key is student's name

std_marks_dict={'pranto':[15,17,15],'akkhar':[12,16,14],'asif':[13,15,18],'bappy':[15,17,16],
                'alamin':[15,16,19]}
print(std_marks_dict['pranto'])
print(std_marks_dict['akkhar'])

std_marks={'pranto':{'bangla':70,'english':80},'akkhar':{'bangla':75,'english':73},
            'bappy':{'bangla':60,'english':75}}

print(std_marks['pranto']['english'])
print(std_marks['bappy']['bangla'])
print(std_marks)