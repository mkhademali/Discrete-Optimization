# # solve each instance
# from solver import solve_it


# def readfile(filename):
#     with open(filename) as thefile:
#         return thefile.read()


# data_instance = readfile('data/ks_100_0')

# print(solve_it(data_instance))


taken = [1, 1, 0, 0]
c = taken.count(0)
while c > 0:
    a = taken.index(1)
    b = taken.index(0)
    taken[a] = 0
    taken[b] = 1
    c = c-1
    print(taken)
