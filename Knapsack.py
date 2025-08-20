capacity = 11
items = [(5,10),(4, 40),(6, 30),(3, 50)]

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

combinations = {}
for i in range(len(items)+1):
    combinations[i] = factorial(len(items)) / (factorial(i)*(factorial(len(items)-i)))

total_comb = 2 ** len(items)

def optimize_knapsack(items:list, capacity: int,i = 0, current_weight = 0, current_score=0, sack=[]):
    if i == len(items):
        return current_score, sack[:]
    
    # No coger
    best_score, best_sack = optimize_knapsack(items,capacity,i+1,current_weight,current_score,sack)

    # Coger
    if current_weight + items[i][0] <= capacity:
        sack.append(items[i])
        take_score, take_sack = optimize_knapsack(items,capacity,i+1,current_weight + items[i][0],current_score + items[i][1],sack)
        sack.pop()

        if take_score > best_score:
            best_score, best_sack = take_score, take_sack

    return best_score, best_sack


print(f"Computer has to calculate {total_comb} different combinations of items.")
print(f"This is because there are {len(items)} items.")
for i in list(combinations):
    print(f"Computer will calculate {int(combinations[i])} combinations of {i} items.")

best_score, best_sack = optimize_knapsack(items,capacity)

print(f"After calculating all those combination, computer found the best posible knapsack is {best_sack}.")
print(f"Which has a value of {best_score}.")