class Operation:

    def __init__(self):
        pass
    
    def add(self, a ,b):
        if not isinstance(a, (int, float)):
            raise ValueError("Value should be int or float")
        
        if not isinstance(b, (int, float)):
            raise ValueError("Value should be int or float")
        return a + b

    def minus(self, a ,b):
        if not isinstance(a, (int, float)):
            raise ValueError("Value should be int or float")
        
        if not isinstance(b, (int, float)):
            raise ValueError("Value should be int or float")
        return a - b
