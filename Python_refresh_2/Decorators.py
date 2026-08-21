def change_case(func):
    def upper():
        return func().upper()
    return upper

@change_case
def get_name():
    return 'python' 
print(get_name())


print ('example of decorator')

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds to execute.")
        return result
    return wrapper

@timer
def train_model():
    time.sleep(2)  # Simulating a time-consuming task
    print("Model trained!")

train_model()