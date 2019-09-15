li=['pranto','anik','asif',1,3]
tpl=(1,4,7)
A=set(li)
B=set(tpl)
print(A, B)

C=set('bangladesh')
print(C)
print('q' in C)

a={'a','c',1}
print('a' in a)

D={'pranto','akkhar','sabbir','bappy','prionti'}
E={'tithi','prionti','sethi','munia'}

z=D&E
print(z)

z=D|E
print(z)

z=D^E
print(z)

z=D-E
print(z)