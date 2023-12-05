from functools import cmp_to_key
def read_file(file):

    with open(file) as f:
        return f.read()

def resolve(left, right):

    
    if type(left) == int and type(right) == int:
        return (left < right) - (left > right)
    
    if type(left) == list and type(right) == list:
        for cmp_val in map(resolve, left, right):
            if cmp_val:
                return cmp_val
        return resolve(len(left), len(right))
            
    if (type(left) == int and type(right) == list) or (type(left) == list and type(right) == int):
        if type(left) == int:
            left  = [left]
        if type(right) == int:
            right = [right]
        return  resolve(left, right)

def main_1(data):

    data = data.split("\n\n")
    data = [(eval(d.split("\n")[0]),eval(d.split("\n")[1])) for d in data]
    s = 0
    for (i,(l,r)) in enumerate(data,1):
         if resolve(l,r) == 1:
            s += i
    print(s)
    keys = [[[2]],[[6]]]
    data = keys + [d for pair in data for d in pair]
    data.sort(key=cmp_to_key(resolve), reverse=True)
    m = 1
    for i,d in enumerate(data, 1):
        if d in keys:
            m *= i
    print(m)

if __name__ == "__main__":
    data = read_file("data.txt")
    main_1(data)
