name = "Cristian"
last_name = "Colorado"
age = "22"
print(name)
print (last_name)

full_name = name + " " + last_name
print (full_name)

#format
template = "Hi, my name is " + name + ", my last name is " + last_name + " and I'm " + age + " years old."
print('v1', template)

template = "Hi, my name is {}, my last name is {} and I'm {} years old." .format(name, last_name, age)
print('v2', template)

template = f"Hi, my name is {name}, my last name is {last_name} and I'm {age} years old"
print('v3', template)