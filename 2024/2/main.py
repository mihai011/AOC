def check_safe(d):
    if d == sorted(d) or d == sorted(d, reverse=True):
        for i in range(len(d)-1):
            diff = abs(d[i]-d[i+1])
            if diff==0 or diff > 3:
                return False
                    
    else:
        return False
    return True

def main1():
    data = open("input.txt", "r").readlines()
    p=0
    for d in data:
        d = [int(c) for c in d.split()]
        if not check_safe(d):
            p+=1
        
    print(len(data)-p)
    
def main2():
    
    data = open("input.txt", "r").readlines()
    p=0
    for d in data:
        d = [int(c) for c in d.split()]
        for i in range(len(d)):
            new_d = d[:i]+d[i+1:]
            if check_safe(new_d):
                p += 1
                break
    print(p)

if "__main__" == __name__:
    main2()