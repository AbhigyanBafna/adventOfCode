inputs = []
oprs = []
ans = 0

with open("input.txt", "r") as file:
    inputs = [line.rstrip('\n') for line in file]
    oprs = [opr for opr in inputs[-1] if not opr.isspace()]
    inputs.pop()

# print(inputs)         
# print(oprs)

# 1. Start to read inputs array from right to left in columns and construct the inputs
# 2. You know a problem has ended i.e you have all the numbers for operation when encounter a line full of spaces
# 3. You fetch the last operator from oprs array and then decrease its index by 1.
# 4. Perform opr on numbers and store result for sum later
# 5. Now repeat the loop and you get correct opr as we are traversing it and have a clear condition to when the problem ends


i = len(inputs[0])-1
n = len(inputs)
nums = []
k = len(oprs)-1

while i >= 0:
    j = 0
    num = ""
    while j < n:
        cand = inputs[j][i]
        if not cand.isspace():
            # print(cand)
            num += cand
        j += 1

    if num == "": #Problem Over
        tans = 0
        if oprs[k] == '*':
            tans = 1
        for l in nums:
            if oprs[k] == '*':
                tans *= l
            else:
                tans += l
        
        k -= 1
        # print("Problem over : ", tans, " And clearing nums")
        ans += tans
        nums = []
    else:
        # print("Appending to nums : ", num)
        nums.append(int(num))

    i -= 1
    
# Adding Last answer
tans = 0
if oprs[k] == '*':
    tans = 1
for l in nums:
    if oprs[k] == '*':
        tans *= l
    else:
        tans += l

# print("Problem over : ", tans, " And clearing nums")
ans += tans

print(ans)