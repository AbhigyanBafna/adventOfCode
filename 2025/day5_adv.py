fresh_ing = []
ans = 0


with open("input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            break

        st, ed = map(int, line.strip().split("-"))
        fresh_ing.append((st, ed))

    print("Fresh Ingredients are : ", fresh_ing)


    fresh_ing.sort()

    while fresh_ing:
        st, ed = fresh_ing.pop(0)
        ans += ed - st + 1

        temp = []
        for lb, ub in fresh_ing:
            if ub > ed:
                temp.append((max(ed + 1, lb), ub))

        fresh_ing = temp

print(ans)