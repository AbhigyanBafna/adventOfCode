# Building Input

arr = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        temp = []
        for char in line:
            temp.append(char)
        arr.append(temp)


# Building Neighbour Matrix
adj = []

a = -1
while a <= 1:
    b = -1
    while b <= 1:
        if a == 0 and b == 0:
            b += 1
            continue
        adj.append((a,b))
        b += 1
    a += 1


n = len(arr)
m = len(arr[0])
ans = 0

def forklift_check(i:int, j: int):

    nbr = []
    for diff in adj:

        temp1 = i+diff[0]
        temp2 = j+diff[1]
        valid = True
        
        if temp1 < 0 or temp2 < 0 or temp1 >= n or temp2 >= m:
            valid = False
        
        if valid:
            nbr.append((temp1, temp2))

    count = 0
    for coord in nbr:
        cand = arr[coord[0]][coord[1]]

        if cand == "@":
            count += 1
        
        if count >= 4:
            return 0

    return 1

stopper = True

def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))


while stopper:

    currRoundValid = 0
    deletion = []

    i = 0
    while i < n:
        j = 0
        while j < m:
            cand = arr[i][j]
            valid = 0

            if cand == "@":
                valid = forklift_check(i,j)

            if valid == 1:
                deletion.append((i,j)) 
                currRoundValid += valid

            j += 1
        i += 1
    
    # print(currRoundValid)
    if currRoundValid == 0:
        stopper = False
    else:
        ans += currRoundValid
        # print(deletion)
        for item in deletion:
            arr[item[0]][item[1]] = "."
        
        print_grid(arr)

print(ans)