fresh_ing = []
ans = 0

with open("input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            break

        st, ed = map(int, line.strip().split("-"))
        fresh_ing.append((st, ed))

    print("Fresh Ingredients are : ", fresh_ing)

    for line in file:
        id = int(line.strip())
        
        for ing_range in fresh_ing:

            if id >= ing_range[0]:
                if id <= ing_range[1]:
                    ans += 1
                    break

print(ans)