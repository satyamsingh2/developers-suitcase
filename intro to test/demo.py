
def area_of_rect(l,b):
    a=l*b
    return a

def area_of_square(a):
    if type(a) is int or type(a) is float:
        return a*a
    else:
        raise TypeError("only int and float allowed")