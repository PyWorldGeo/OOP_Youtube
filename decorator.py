from time import time

class Decorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        start = time()
        print("Start time:", start)
        self.function()
        end = time()
        print("End time:", end)
        print("Time needed to execute:", end-start)

@Decorator
def func1():
    i = 0
    while i < 1000:
        print("Function 1")
        i += 1


func1()

# dec = Decorator(func1)
# dec()