my_table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
   print(my_table[0][0])
# lists are mutable, so we can do this
my_table[0][0] = 42
print(my_table)

my_2d_list = [
    [0],
    [1, 2, 3, 4],
    [5, 6],
]
print(my_2d_list)


my_3d_list = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print(my_3d_list[0][0][0])
