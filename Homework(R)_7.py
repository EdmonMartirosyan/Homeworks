def answer_queries(k, *query_counts):
    balance = 0
    day = 0
    for elem in query_counts:
        day += 1
        if elem > k:
            balance += elem-k
        elif elem < k:
            b = balance
            if balance > 0:
                balance -= k-elem
        if balance <= 0 and b+elem != k:
            return day
    while balance >= 0:
        balance -= k
        day += 1
    return day


print(answer_queries(5, 10, 5, 5, 3, 2, 1))