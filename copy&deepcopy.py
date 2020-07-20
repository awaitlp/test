from copy import copy,deepcopy

######################


###########
a = [1,2,3,4,[1,2]]

b = copy(a)

c = deepcopy(a)

print(a)
print(b)
print(c)

print('===================')

a[-1].append(10)

print(a)
print(b)
print(c)
