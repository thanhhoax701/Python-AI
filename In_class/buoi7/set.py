set1 = {1,7,3,5,2,1,3}
print(set1)

set2 = {1, 5.0, "Hello", (1,2,3)}
print(set2)

set3 = set()
print(set, "\n")


A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

print(A | B)
print(A.union(B))

print(A & B)
print(A.intersection(B))

print(A - B)
print(A.difference(B))

print(A ^ B)
print(A.symmetric_difference(B))