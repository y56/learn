def maximumTotalWeight(tasks, weights, runtime):
    items = [[tasks[i]*2,weights[i]] for i in range(len(tasks))]
    knapsackValues = [[0 for _ in range(runtime+1)] for _ in range(len(items)+1)]
    for i in range(1, len(items)+1):
        duration, value = items[i-1]
        for d in range(1, runtime+1):
            if duration > d:
                knapsackValues[i][d] = knapsackValues[i-1][d]
            else:
                knapsackValues[i][d] = max(knapsackValues[i-1][d], knapsackValues[i-1][d-duration]+value)
    return knapsackValues[-1][-1]
