distinct_terms = []

for i in range(2, 101):
    for j in range(2, 101):
        dis_term = i ** j
        distinct_terms.append(dis_term)

distinct_terms = set(distinct_terms)
print(len(distinct_terms))
