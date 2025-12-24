tach_m = []

with open("input.txt", "r") as file:
    for line in file:
        tach_m.append(list(line.strip()))

#Initialize Tach Beam
i = 0

mani_l = len(tach_m)
grid_l = len(tach_m[0])

while i < grid_l:
    pos = tach_m[0][i]

    if pos == 'S':
        # print("Found Tach Beam!")
        tach_m[1][i] = '|'

    i += 1

ans = 0
i = 2

while i < mani_l:
    # print("In outer Loop with i : ", i)
    j = 0
    while j < grid_l:
        # print("In inner Loop with j : ", j)

        up = tach_m[i-1][j]
        cur = tach_m[i][j]

        if up == '.' or up == '^':
            j += 1
            continue

        if up == '|':
            if cur == '^':
                # print("Beam Splitting!")
                ans += 1
                if j-1 >= 0:
                    tach_m[i][j-1] = '|'

                if j + 1 < grid_l:
                    tach_m[i][j+1] = '|'
            else:
                tach_m[i][j] = '|'
        
        j += 1
    
    i += 1
                

print(ans)


# for l in tach_m:
#     print(" ".join(l))
#     print()
