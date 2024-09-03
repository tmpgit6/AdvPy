# The order is a MUST

def greeting(num1, num2 , num3 = 50, *xargs, **kwargs):
    print(num1, num2 , num3 , xargs, kwargs) 

def greeting3(num1, num2,/, num3 = 3,*, num4 =4, num5 = 5):
    print(num1, num2, num3,num4, num5)




greeting(1,2 ,3,4,5,6,7,8,9, car="VW", bj ="2020")

greeting3(1,2,30, num4=40, num5=50)