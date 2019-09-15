# class car:
#     name='audi'
#     color='black'
#     def start():
#         print('starting the engine')
# print('name of the car:',car.name)
# print('color of the car:',car.color)
# car.start()




    # #another work

# class car1:
#     name=''
#     color=''
#     def start(self):
#         print('starting the engine')
# car1.name='bmw'
# car1.color='white'
# print('name of the car:',car1.name)
# print('color of the car:',car1.color)
# car1.start()
# car1.name='toyota'
# car1.color='red'
# print('name of the car:',car1.name)
# print('color:',car1.color)
# car1.start()

    #creating car1 object
# my_car=car1()
# my_car.name='allion'
# my_car.color='blackwhite'
# print('name of the car:',my_car.name)
# print('color:',my_car.color)
# my_car.start()



    #new steps of object class:

# class car:
#     name=''
#     color=''

#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def start(self):
#         print('starting the engine')
# my_car=car('corolla','white')
# print(my_car.name)
# print(my_car.color)
# my_car.start()

  #object steps part 2

# class car:

#     def __init__(self,n,c):
#        self.name=n
#        self.color=c

#     def start(self):
#         print('starting car engine')

# my_car=car('corola','black')
# print(my_car.name)
# print(my_car.color)
# my_car.start()

  #another step part 3:

# class car:
#     def __init__(self,n,c,m):
#         self.name=n
#         self.color=c
#         self.make=m
#     def start(self):
#         print('starting car engine')
#         print('car name:',self.name)
#         print('car color:',self.color)
#         print('making date:',self.make)
# my_car=car('bugati','blue','20/4/2002')
# my_car.start()
# my_car1=car('toyota','white','12/5/2004')
# my_car1.start()
# my_car2=car('nano','black','20/5/2003')
# my_car2.start()

#exercise

class car:
    def __init__(self,n,m,c,y,cc):
        self.name=n
        self.manufacturer=m
        self.color=c
        self.year=y
        self.cc=cc
    def start(self):
        print('start the engine')
        print('car name:',self.name)
        print('made by:',self.manufacturer)
        print('car color:',self.color)
        print('production date:',self.year)
        print('engine speed',self.cc)

    def brake(self):
        print('push me!')
    def drive(self):
        print('i run my audi A6')
    def turn(self):
        print('turn me!')
    def change_gear(self):
        print('please change gear')

new_car=car('Audi','Volkswagen Group','black','1932','2500')
# print(new_car.name)
new_car.start()




    