def main1():
    
    data = open("input.txt").readlines()
    l1, l2 = [], []
    for d in data:
        d = d.split()
        l1.append(int(d[0]))
        l2.append(int(d[-1]))
    
    
    l1.sort()
    l2.sort()
    pairs = zip(l1, l2)
    diffs  = [abs(a-b) for a, b in pairs]
    print(sum(diffs))
    
def main2():
    data = open("input.txt").readlines()
    l1, l2 = [], []
    for d in data:
        d = d.split()
        l1.append(int(d[0]))
        l2.append(int(d[-1]))
    
    
    l1.sort()
    l2.sort()
    diffs  = [a* (l2.count(a)) for a in l1]
    print(sum(diffs))
        
if __name__ == '__main__':
    main1()
    main2()