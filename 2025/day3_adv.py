
def find_joltage(battery: str, length: int):
    print("Doing ops for : ", battery)
    n = len(battery)
    limiter = 0
    jolt = ""

    for k in range(length,0,-1):
        # print("Running for k : ", k)
        # print("Limiter is : ", limiter)

        i = limiter
        j = limiter+1
        maxP = limiter

        # print("Starting pointers at : ", i , j)
        while(j <= n-k):
            num1 = int(battery[i])
            num2 = int(battery[j])
            # print("Comparing nums in while loop", num1, num2)
            # print("Valye of j in while :", j)

            if num1 > num2:
                if num1 > int(battery[maxP]):
                    maxP = i
            else:
                if num2 > int(battery[maxP]):
                    maxP = j

            i += 1
            j += 1
        
        limiter = maxP+1
        jolt += battery[maxP]
        # print("Jolt is : ", jolt)

        # print("Max Pointer is in search space is ", maxP)

    return int(jolt)



with open("input.txt", "r") as file:
    ans = 0
    length = 12
    for line in file:
        battery = line.strip()
        joltage = find_joltage(battery, length)
        ans += joltage

print(ans)
        

