data = ""
with open("input.txt", "r") as file:
    data = file.read().replace("\n", "")

arr = [tuple(map(int, item.split("-"))) for item in data.split(",")]

ans = 0
for item in arr:
    for i in range(item[0], item[1]+1):
        num = str(i)
        # print("Running for num : ", num)

        n = len(num)
        half = n // 2
        for j in range(1,half+1):
            cand = num[:j]
            step = len(cand)
            if n % step != 0:
                continue

            # print("Current Candidate and j : ", cand, " ", j)
            
            k = j
            validCand = True

            while k<=n and k + step <= n:
                sliceAt = k + step
                nextCand = num[k:sliceAt]
                # print("NextCandidate against Candidate is ", nextCand)
                if cand != nextCand:
                    validCand = False
                    break
                k += step

            if validCand:
                # print("Selected Cand : ", i)
                ans += i
                break
    
print(ans)