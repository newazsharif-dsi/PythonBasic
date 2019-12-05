variables = ["one", "two", "three", "four", "five"]

# Negative index starts from the back of the list
print(variables[-4])


#If we want to return the elements from i index to end index, syntax will be variables[i:]
print(variables[2:])


#If we want to return the elements from i index to j-1 index, syntax will be variables[i:j]
print(variables[1:3])


#i:j:step example
print(variables[0:5:2])


#add a list
numbers = [7,4,5,6,8,9,10,11,2,5]
variables.extend(numbers);
print(variables)

#append an element to a list
variables.append("Newaz")
print(variables)

#insert into a list, if an element is inerted in ith index then all of the elements from ith index to end will be shifted to right
variables.insert(3,"Hello");
print(variables)

#Remove the last element
last_element = variables.pop()
print(variables)
print(last_element)
#
