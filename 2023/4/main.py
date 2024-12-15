
def main():

    data = open("input.txt").read().split("\n")
    s = 0
    for d in data:
        d = d.replace(":", "|")
        d = d.split("|")
        winnning_numbers = set([int(n) for n in d[1].strip().split(" ") if n != ""])
        have_numbers = set([int(n) for n in d[2].strip().split(" ") if n != ""])
        common = winnning_numbers.intersection(have_numbers)
        if not common:
            continue
        s += 2 ** (len(common) - 1)
    print(s)
        
def main2():
    data = open("input.txt").read().split("\n")
    common_lists = []
    for d in data:
        d = d.replace(":", "|")
        d = d.split("|")
        winnning_numbers = set([int(n) for n in d[1].strip().split(" ") if n != ""])
        have_numbers = set([int(n) for n in d[2].strip().split(" ") if n != ""])
        common = winnning_numbers.intersection(have_numbers)
        common_lists.append(len(common))
    total_cards = [1 for i in range(len(common_lists))]
    for i in range(len(total_cards)):
        for j in range(i+1, i+1+common_lists[i]):
            total_cards[j] += total_cards[i] 
    print(sum(total_cards))
    

if __name__ == "__main__":
    main()
    main2()

