#complex datatypes: for creating complex numbers 
#complex number comprises 2 parts

#1.realpart ------> float type
#2.imaginary part-> float type 

x=3+4j
print(x)
print(type(x))
print(id(x))

print(x.real)
print(x.imag)

#we can also create complex numbers by using complex() function:
x=complex(3,-4)
print(x)

y=complex(0.3,0.4)
print(y)

z=complex(3)
print(z)

w=complex('3-4j')
print(w)




