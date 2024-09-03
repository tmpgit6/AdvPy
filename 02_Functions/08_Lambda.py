# 1. classical way
def doubler(num):
    return num * 2 

print(doubler(10))




# 2. Lambda function
banana = lambda num : num * 2
print(banana(220))


##########################################
# Special Sorting (key)

items = [
            ("Product A", 60) , 
            ("Product B", 50) , 
            ("Product C", 70)
         ]


items.sort(key = lambda item: item[1])
print(items)
items.sort(key = lambda item: item[1], reverse= True) 


############################################
# Filter
my_list = [1,5,6,7,9,10,11,12,13]
result = list(filter(lambda num: (num%2 == 0),  my_list))
print(result)



# Map
my_list = [1,5,6,7,9,10,11,12,13]
result = list(map(lambda num: num * 2,  my_list))
print(result)



