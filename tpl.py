items=(1,4,1.5,('pranto','b','c'),['apple','mango'])
for item in items:
    print (item,type(item))
print('the tuple item is sorted:',items[3][2])

tp=('pranto','anik','shahed', (1,4,7))
print(tp[3][0])

tp1=(1,5,9,0)
li=list(tp1)
print(li)
print(1 in tp1)