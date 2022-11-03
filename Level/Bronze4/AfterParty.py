Count, Area = map(int, input().split())
A, B, C, D, E = map(int, input().split())

People = Count * Area

print(A - People, B - People, C - People, D - People, E - People)