import collections

def propogate_tach(tach, split):
    new_tach = collections.defaultdict(int)
    for tach_pos, tach_count in tach.items():
        if tach_pos in split:
            new_tach[tach_pos-1] += tach_count
            new_tach[tach_pos+1] += tach_count
        else:
            new_tach[tach_pos] += tach_count
    
    return new_tach


with open("input.txt", "r") as file:

    start_l = file.readline()
    start_c = start_l.index('S')
    paths = {}
    paths[start_c] = 1
    # print("Starting with 1 path at S")
    splitters = []

    for line in file:
        new_split = set([idx for idx, char in enumerate(line) if char == "^"])
        if new_split:
            splitters.append(new_split)


for l in splitters:
    paths = propogate_tach(paths, l)    


print(sum(paths.values()))