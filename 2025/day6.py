inputs = []
oprs = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        # print("Unprocessed Line : ", line)
        input1 = []
        num = True
        start = True

        p = 0
        n = len(line.strip())
        # print("Length of line : ", n)

        while p < n :
            # print(f"In Loop with vars p {p}, num {num}, start {start}")
            # print("Line Processed Input1 : ", input1)
            if start:
                if not line[p].isdigit():
                    num = False
                start = False
            
            while p < n and line[p] == " ":
                p += 1
            
            if p >= n:
                break

            inp = ""
            while p < n and line[p] != " ":
                inp += line[p]
                p += 1
            
            if num:
                input1.append(inp)
            else:
                oprs.append(inp)
        
        if num:
            inputs.append(input1)
    

print(inputs)         
print(oprs)

ans = 0

i = 0

while i < len(oprs):
    opr = oprs[i]
    inps = []
    for inp in inputs:
        inps.append(int(inp[i]))

    temp = 0
    if opr == "*":
        temp += 1
        for inp in inps:
            temp *= inp
    else:
        for inp in inps:
            temp += inp
    
    ans += temp
    i += 1

print(ans)