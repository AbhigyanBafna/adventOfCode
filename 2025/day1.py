pointer = 50
ans = 0

def process(newAns: int, curr: int, input: str):
    print("Starting Process with pointer : ", curr, " input : ", input, " Answer : ", newAns)
    dir = input[0]
    disp = int(input[1:])
    change = disp % 100

    if dir == "R":
        curr += change
        if curr >= 100:
            curr -= 100
    else:
        curr -= change
        if curr < 0:
            curr +=100

    return newAns, curr
        
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        newAns, pointer = process(ans, pointer, line)
        ans = newAns
        print("Current Value after Process : ", pointer, " Ans : ", ans)
        if pointer == 0:
            ans += 1

print(ans)