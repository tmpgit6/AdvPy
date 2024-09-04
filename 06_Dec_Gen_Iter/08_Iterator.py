class MyRange():

    def __init__(self,start, end) -> None:
        self.current = start 
        self.end = end 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if self.current >= self.end:        
                raise StopIteration("No More Elements") 
        except StopIteration:
            print("Done")
        else:
        
            current = self.current
            self.current += 1 
            return  current
   
    def __del__(self):
        return self


# for num in MyRange(1,5):
#     print(num)

my_ranger = MyRange(1,4)
print(next(my_ranger))
print(next(my_ranger))
print(next(my_ranger))
print(next(my_ranger))