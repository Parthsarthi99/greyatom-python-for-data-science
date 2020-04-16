# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio' ]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = (class_1 + class_2)
print (new_class)


# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Code ends here


# --------------
# Code starts here
#Create dictionary and add keys and values to it
courses = {'Math': 65, 'English': 70, 'History': 80, 'French': 70, 'Science': 60}

#print the marks
print(courses)

#Calculate total
total = sum(courses.values())

#Print toatl marks scored
print(total)

#Percentage Calculation
percentage = (float(total/500) ) *100

#print Percentage
print(percentage)

# Code ends here


# --------------
# Code starts here

#Create Dictionary and add values and keys to it
mathematics = {'Geofrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65, 'Yoshua Benjio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}

#Finding the topper
topper = max(mathematics, key = mathematics.get)


#Print the topper
print(topper)



# Code ends here  


# --------------
# Given string
topper = ' andrew ng'


# Code starts here
#Splitting the toppers name to First name and last name
first_name = topper.split()[0]
last_name = topper.split()[1]
last_name = 'ng'

#Create full name
full_name = (last_name + ' ' + first_name)

#Converting full name to upper case
certificate_name = full_name.upper()

#print certificate name
print(certificate_name)
# Code ends here


