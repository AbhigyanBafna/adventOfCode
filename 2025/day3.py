
def find_joltage(battery: str):
    print("Doing ops for : ", battery)
    n = len(battery)
    maxP = 0
    minP = n-1

    for i in range(1,n-1):
        num = int(battery[i])

        if num > int(battery[maxP]):
            maxP = i
        
    print("Max Pointer is ", maxP)

    for j in range(n-2, maxP, -1):
        num = int(battery[j])

        if num > int(battery[minP]) and maxP != j:
            minP = j

    jolt = int(battery[maxP] + battery[minP])
    print(jolt)

    return jolt



with open("input.txt", "r") as file:
    ans = 0
    for line in file:
        battery = line.strip()
        joltage = find_joltage(battery)
        ans += joltage

print(ans)
        

