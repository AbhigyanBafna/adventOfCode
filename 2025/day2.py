data = ""
with open("input.txt", "r") as file:
    data = file.read().replace("\n", "")

arr = [tuple(map(int, item.split("-"))) for item in data.split(",")]

ans = 0
for item in arr:
    for i in range(item[0], item[1]+1):
        num = str(i)
        n = len(num)
        half = n // 2

        if n % 2 == 0:
            f = num[:half]
            l = num[half:]
            if f == l:
                ans += i
    
print(ans)