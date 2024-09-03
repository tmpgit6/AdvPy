course = "Python"
course = 'Python'


first_name = "Thomas"
last_name = "Meier"

# Vorname: Thomas - Nachname: Meier

#1. String Concatenation
full_name = "Vorname:" + " " + first_name, "-", "Nachname: " + last_name


print("Vorname:" + " " + first_name, "-", "Nachname: " + last_name)


#2. String Formatting
full_name = "Vorname: {} - Nachname: {}".format(first_name, last_name)
print(full_name)

full_name = f"Vorname: {first_name} - Nachname: {last_name}"
print(full_name)


print("=" * 30)

#################################################

course_name = "Python" # Python Style
COURSE_NAME = "Python" # Python Style Constant
Course = "Python" # Class
 
#.course()

_sum = 0
###########################

user = {"id": 100,
        "name": "Thomas",
        "age": 42,
        "kids": ["Julia", "Lena"],
        "kids2":[
                    {"id": 1000, "first_name":"Julia", "friends": ["Max","Frank"]}, 
                    {"id": 1001, "first_name":"Lena", "friends": ["Sara","Lena"]}, 
        
                 
                 ]
        }
print(user["kids2"][0]["friends"][0]) # Max





for key in user.keys():
    print(key)

for value in user.values():
    print(value)

    
for item in user.items():
    print(item)

for key,val in user.items(): #(key, value)
    print(key,val)

for key in user:
    print(key)



print(user)
# print(user["cars"])
print(user.get("cars"))
print(user.get("cars", "It is not found"))