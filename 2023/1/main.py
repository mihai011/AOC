def main1():
    data = open("input.txt").read().split("\n")
    s = 0
    for d in data:
        d = [c for c in d if c.isdigit()]
        s += int("".join([d[0], d[-1]]))

    print(s)


def main2():
    data = open("input.txt").read().split("\n")
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    l_digits = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "zero",
    ]

    s = 0
    for d in data:
        pos = []
        for symbol in digits:
            if symbol in d: 
                pos += [(symbol, index) for index in range(len(d)) if d.startswith(symbol, index)]
        for i, symbol in enumerate(l_digits):
            if symbol in d:
                pos += [(str(i), index) for index in range(len(d)) if d.startswith(symbol, index)]

        pos.sort(key = lambda x: x[1])
        if pos:
            s += int(''.join([pos[0][0], pos[-1][0]]))
        
    print(s)


if __name__ == "__main__":
    main1()
    main2()
