

from zoneinfo import available_timezones


def read_data():
    
    data = open("input.txt").read().split("\n")
    games = []
    for d in data:
        d = d.split(";")
        game = []
        for s in d:
            s = s.split(" ")
            set_dict = {}
            for i in range(len(s)):
                if s[i].startswith("red"):
                    set_dict["red"] = int(s[i-1])
                if s[i].startswith("blue"):
                    set_dict["blue"] = int(s[i-1])
                if s[i].startswith("green"):
                    set_dict["green"] = int(s[i-1])
                    
            game.append(set_dict)
        games.append(game)
        
    return games

def main1():
    
    games = read_data()
    
        
    available_cubes = {"red": 12, "blue":14, "green":13}
    ids = 0
    for i, game in enumerate(games):
        pos_game = True
        for set in game:
            for k,v in set.items():
                if available_cubes[k] < v:
                    pos_game = False
        if pos_game:
            ids += i +1
    print(ids)
    
def main2():
    
    games = read_data()
    ids = 0
    for i, game in enumerate(games):
        m_dict = {"red": 0, "blue":0, "green":0}
        for set in game:
            for k,v in set.items():
                m_dict[k] = max(m_dict[k], v)
                
        ids += m_dict["red"] * m_dict["blue"] * m_dict["green"]
        
    print(ids)
            
    
if __name__ == "__main__":
    main1()
    main2()