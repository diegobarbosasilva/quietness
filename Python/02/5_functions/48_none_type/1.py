a = None

print(type(a))      # ~ NoneType

def subtract(a, b):
    print(a - b)

result = subtract(5, 3)     # & Assign result of a function call, where the function has NO return
print(result)               # ~ 2 
                            # ~ None