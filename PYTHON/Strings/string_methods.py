#string methods:

#1. upper(): for printing a string in uppercase 
x='banglore'
print(x.upper())

#2. lower(): for printing a string in lowercase 
x='BGL'
print(x.lower())

#3. capitalize(): for capitalizing the 1st character of a string
x='india'
print(x.capitalize())

#4. title(): for capitalizing 1st character of each word in a file
x='good morning'
print(x.title())

#5. swapcase(): for converting one case to another case 
x='Good morning hyderabad'
print(x.swapcase())

#6. replace(): for replacing a portion of a string 
x='java is easy to learn'
print(x.replace('java', 'python'))


#7. count(): to count the number of occurrences of each sub-string or a character
x="hello hello hello.... how are you"
print(x.count("hello"))

#8. format(): for substitutions 
x="{} is the captain of IndianTeam"
print(x.format("Dhoni"))

#9. split(): if we split a string, we get a list 
x='hello good morning'
y='101,james,8999,manager,pune'
print(x.split())
print(y.split(','))

#10. strip(): for removing the backspaces before and after the string

x = " hello good evening "
#print(x.strip())
y=x.strip()
print(y)

#11. find(): to check whether a sub-string is available or not 
#if found it returns the 1st character index position of the sub-string else it returns -1.

x='python is easier than java'
print(x.find('java'))
print(x.find('hadoop'))

# startswitch
# endswith 

print(x.startswith('python'))
print(y.endswith('java'))

#12. isapha(): to check whether all the characters within the string are alphabets
date='agu05'
print(date.isalpha())

#13. isdecimal(): to check whether all the characters within the string are numeric

date='agu05'
print(date.isdecimal())

city='bangalore'
print(city.isdecimal())

x='27 10 2021'
print(x.isdecimal())

# accno=8398304
# print(accno.isdecimal())

pi='3.4'
print(len(pi))
print(pi.isdecimal())

#14. isalnum(): to check whether all the characters within the string are alphabets or numeric

date='agu05'
print(date.isalnum())

city='bangalore'
print(city.isalnum())

x='27 10 2021'
print(x.isalnum())

# accno=8398304
# print(accno.isdecimal())

pi='3.4'
print(len(pi))
print(pi.isalnum())

#15. casefold(): for converting into lowercase 
x='Wellcom to python world'
print(x.casefold())

#16. partition(): it always returns tuple of 3 strings
# i) before match ii) Match  iii) After match 

cities = 'MUMBAI HYD CHENNAI'
y=cities.partition('HYD')
print(y)

cities = 'MUMBAI HYD CHENNAI BGL'
y=cities.partition('BGL')
print(y)

#17. join(): joins the elements of a iterable (list/tuple/set/dict) into one string
emps = ['ajay', 'rohit', 'james', 'blake', 'george']
x=" ".join(emps)
print(x)
y="\t".join(emps)
print(y)

date=['28', '10', '2025']
d=' '.join(date)
print(d)

x='/'.join(date)
print(x)