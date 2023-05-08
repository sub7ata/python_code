from functools import reduce
sequences = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, sequences)
print(product)
print(reduce(lambda x, y: x+y, sequences)) ##addition of products