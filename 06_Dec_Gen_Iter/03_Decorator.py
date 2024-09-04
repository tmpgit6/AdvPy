import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() 

        print(f"Time: {end - start:.4f}", )
        return result
    
    return wrapper

@timer         
def slow_function(seconds):
    time.sleep(seconds)
    return "Done"


slow_function(2)