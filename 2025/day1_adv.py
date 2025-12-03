pointer = 50
ans = 0

def process(newAns: int, curr: int, input: str):
    print("Starting Process with pointer : ", curr, " input : ", input, " Answer : ", newAns)
    dir = input[0]
    disp = int(input[1:])
    q = disp // 100
    newAns += q # Counts Purely Round Trip Occurances of 0.
    change = disp % 100


    if dir == "R":
        if curr + change > 100 and curr != 0: 
            newAns += 1 # Counts Purely Single Jump Occurances of 0.
        curr += change
        if curr >= 100:
            curr -= 100
    else:
        if curr - change < 0 and curr != 0:
            newAns += 1 # Counts Purely Single Jump Occurances of 0.
        curr -= change
        if curr < 0:
            curr +=100

    return newAns, curr
        
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        oldP = pointer
        newAns, pointer = process(ans, pointer, line)
        ans = newAns
        print("Current Value after Process : ", pointer, " Ans : ", ans)
        if pointer == 0 and oldP != pointer: # The oldP != pointer comparision is for cases where round trip from 0 which the quotient calc. will handle.
            ans += 1 # Counts Purely Final Landing Occurances of 0.

print(ans)