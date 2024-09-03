mylist = [1,2,3,4,5,6,7]

num1,num2,num3 =  mylist[0:3]

num1,num2, *other, num7 = mylist

print(num1,num2, other, num7 )
print(num1,num2, *other, num7 )
