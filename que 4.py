xs=[1, 2.3, 5.6, 7, 78]
def solve(xs):
    m = 45
    c = 0.5
    for x in xs:
        y = m * x + c
        print(y)

print(solve(xs))
