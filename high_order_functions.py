from functools import reduce


my_list = [1,4,5,6,9,13,19,21]
my_reduce_list = [2,2,2,2,2]

odd = [i for i in my_list if i % 2 != 0]

# Filter
filter_odd = list(filter(lambda number: number%2 != 0, my_list))

# Map
map_squares = list(map(lambda number: number**2, my_list))

# Reduce
reduce_multiply = reduce(lambda actual_value, next_value: actual_value*next_value, my_reduce_list)

if __name__ == '__main__':
  print(my_list)
  print(filter_odd)
  print(map_squares)
  print(reduce_multiply)