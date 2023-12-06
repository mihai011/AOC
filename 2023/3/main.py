

def main():
    data = open("input.txt").read().split("\n")
    sym_pos = []
    groups = []
    groups_pos = []
    for i in range(len(data)):
        current_group = []
        current_group_pos = []
        for j in range(len(data[i])):
            if not data[i][j].isdigit() and data[i][j] != ".":
                sym_pos.append((i, j))
            if data[i][j].isdigit():
                current_group.append(data[i][j])
                current_group_pos.append((i, j))
            if  not data[i][j].isdigit() or j == len(data[i]) - 1:
                if current_group:
                    groups.append(int("".join(current_group)))
                    groups_pos.append(current_group_pos)
                    current_group = []
                    current_group_pos = []

    found_groups = set()
    for pos in sym_pos:
        for a_pos in [
            [pos[0] + 1, pos[1]],
            [pos[0], pos[1] + 1],
            [pos[0] - 1, pos[1]],
            [pos[0], pos[1] - 1],
            [pos[0] + 1, pos[1] + 1],
            [pos[0] + 1, pos[1] - 1],
            [pos[0] - 1, pos[1] + 1],
            [pos[0] - 1, pos[1] - 1],
        ]:
            if not a_pos[0] < 0 and not a_pos[1] < 0 and not a_pos[0] > len(data) - 1 and not a_pos[1] > len(data[0]) - 1:
                for i in range(len(groups_pos)):
                    if tuple(a_pos) in groups_pos[i]:
                        found_groups.add(i)
                    
    print(sum([groups[i] for i in found_groups]))

def main2():
    data = open("input.txt").read().split("\n")
    sym_pos = []
    groups = []
    groups_pos = []
    for i in range(len(data)):
        current_group = []
        current_group_pos = []
        for j in range(len(data[i])):
            if data[i][j] == "*":
                sym_pos.append((i, j))
            if data[i][j].isdigit():
                current_group.append(data[i][j])
                current_group_pos.append((i, j))
            if not data[i][j].isdigit() or j == len(data[i]) - 1:
                if current_group:
                    groups.append(int("".join(current_group)))
                    groups_pos.append(current_group_pos)
                    current_group = []
                    current_group_pos = []

    s = 0
    for pos in sym_pos:
        found_groups = set() 
        for a_pos in [
            [pos[0] + 1, pos[1]],
            [pos[0], pos[1] + 1],
            [pos[0] - 1, pos[1]],
            [pos[0], pos[1] - 1],
            [pos[0] + 1, pos[1] + 1],
            [pos[0] + 1, pos[1] - 1],
            [pos[0] - 1, pos[1] + 1],
            [pos[0] - 1, pos[1] - 1],
        ]:
            if not a_pos[0] < 0 and not a_pos[1] < 0 and not a_pos[0] > len(data) - 1 and not a_pos[1] > len(data[0]) - 1:
                for i in range(len(groups_pos)):
                    if tuple(a_pos) in groups_pos[i]:
                        found_groups.add(i)
                    
        if len(found_groups) == 2: 
            p = 1
            for i in found_groups:
                p *= groups[i]
            s += p
            
    print(s)
                    

if __name__ == "__main__":
    main()
    main2()
