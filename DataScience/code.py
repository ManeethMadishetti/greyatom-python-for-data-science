# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
# Concatenate both the strings
class_2=[ 'Hilary Mason','Carla Gentry','Corinna Cortes']

# Append the list
new_class=class_1+class_2
# Print updated list
print(new_class)

# Remove the element from the list
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Print the list



# Create the Dictionary

courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}

total=sum(courses.values())
print(total)
percentage=(total/500)*100
print(percentage)
# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':	95,'Sebastian Raschka':	65,'Yoshua Benjio':	50,'Hilary Mason':	70,'Corinna Cortes':	66,'Peter Warden':	75}
topper=max(mathematics,key=mathematics.get)
print(topper)

first_name=topper.split()[1]
last_name=topper.split()[0]


full_name=(first_name+" "+last_name)

certificate_name=full_name.upper()

print(certificate_name)
# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


