print(int(3.14)) #convert float to int
print(float(4)) #convert int to int
s="A"
c=ord(s)
print(c) #convert a charecter to int
x=100
y=str(x)
print(y)
print(type(y)) #convert int to string
tup1="python"
a=tuple(tup1)
print(a) #string converted tuple function, any data in (bracket) is tuple
b="python"
b=set(b)
print(b) #string convert into set, any data in {brases} will be set
d="python"
d=list(d)
print(d) #string converted into list, any data in [square] will be list
tup=(('g',1),('h',2))
n=dict(tup)
print(n)