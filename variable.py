#day2: 30 days of python programming
first_name="busisa"
last_name="ignatius"
full_name="busisa ignatius"
country="road"
city="newyork"
age="19"
year="2026"
is_married="not yet"
is_true="true"
is_light_on="maybe"
first_name, last_name, full_name="busisa","ignatius","busisa ignatius"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

if len(first_name) > len(last_name):
    print("nama depan lebih panjang")
elif len(first_name) < len(last_name):
    print("nama belakang lebih panjang")
else:
    print("panjang nama sama")


num_one=5
num_two=4
variable_total=num_one+num_two
print(variable_total)
variable_diff=num_one-num_two
print(variable_diff)
variable_product=num_two*num_one
print(variable_product)
variable_division=num_one/num_two
print(variable_division)
variable_remainder=num_two%num_one
print(variable_remainder)
variable_exp=num_one**num_two
print(variable_exp)
floor_division=num_one//num_two
print(floor_division)

r=float(input("r="))
pi=3.14
area_of_circle=pi* r**2
print(f"area of circle is {area_of_circle}")
circum_of_circle=2*pi*r
print(circum_of_circle)

nama_depan=input("masukan nama depan")
nama_belakang=input("masukan nama belakang")
negara_asal=input("negara asal")
umur=int(input("masukan umurmu"))
