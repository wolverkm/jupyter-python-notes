# Given a list of strings, find their corresponding lengths
# filename: debugging_demo1.py
def what1(x):
    res = []
    for w in x:
        res.append(len(w))
    return res

a = [ 'apple', 'pineapple', 'fig', 'mangoes' ]
b = what1(a)
print(b) 