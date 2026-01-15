#no.11
x=float(input('masukan nilai x= '))
y=x**2+6*x+9
print(y)

#no.12
print(len('python') > len('dragon'))

#no.13
print('on' in'python' and 'on' in 'dragon')

#no.14
print('jargon' in 'I hope this course is not full of jargon')

#15
print(not 'on' in 'python'and 'on' in 'dragon')

#no.16
text=float(len('python'))
text1=str(text)
print(text1)

#no.17
event_number=int(input('Even numbers are divisible by 2 and the remainder is zero= '))
if event_number%2==0:
    print('your input is true')
else:
    print('your input is false')

#no.18
print(7//3==int(2.7))

#no.19
print('ten'==10)

#no.20
print(int(9.8)==10)

#no.21
work_hours=int(input('enter work hours= '))
rate_per_hours=int(input('enter rate per hours= '))
print('your weekly earning is: ', work_hours*rate_per_hours)

#no.22
years_lived=float(input('enter your age= '))
if years_lived<=100:
    seconds=60*60*24*365
    print('you have lived= ',years_lived*seconds)
else :print('enter correctly!')

#no.23
for i in range (1,6):
    print(i,1,i**2,i**3)