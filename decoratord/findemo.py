
def smart_function(fn):
    def same_code(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return same_code  # () is not needed for calling inner function

@smart_function
def sub(n1,n2):
    return n1-n2

@smart_function
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(div(10,20))