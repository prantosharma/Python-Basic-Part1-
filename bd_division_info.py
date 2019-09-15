bd_dividion_info={}
bd_dividion_info['dhaka']={'district':13,'upozila':93,'union':1833}
bd_dividion_info['chattogram']={'district':11,'upozila':97,'union':336}
bd_dividion_info['barisal']={'district':6,'upozila':39,'union':333}
bd_dividion_info['khulna']={'district':10,'upozila':59,'union':270}
bd_dividion_info['mymensingh']={'district':4,'upozila':34,'union':350}
bd_dividion_info['rajshahi']={'district':8,'upozila':70,'union':558}
bd_dividion_info['rangpur']={'district':8,'upozila':58,'union':536}
bd_dividion_info['sylhet']={'district':4,'upozila':38,'union':334}

print(bd_dividion_info)
divisions=bd_dividion_info.keys()
print(divisions)

#using for loop
for division in divisions:
    print('division:',division)

#upazila
for division in divisions:
    print(division,'upazila',bd_dividion_info[division]['upozila'])

#print only keys
for i in bd_dividion_info:
    print('Division is:',i)

#print keys and it's value
for items in bd_dividion_info:
    print(items)
    print(bd_dividion_info[items])
#2nd type
for key,value in bd_dividion_info.items():
    print(key)
    print(value)

#print all district,upazila,union from bd_divisions_info 
for division in divisions:
    print(division,'district',bd_dividion_info[division]['district'])
    print(division,'upazila',bd_dividion_info[division]['upozila'])
    print(division,'union',bd_dividion_info[division]['union'])
