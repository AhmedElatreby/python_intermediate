# def count(x):
#     y = x  + 10
#     return y

# print(count(10))

# Lambda function
# x = lambda y : y + 10 
# print(x(10))


# using add function
num = [1,2,3,4,5,6,7,8,9]

# def count(x):
#     y = x + 10
#     return y

# add = map(count, num)

# print(list(add)) # [11, 12, 13, 14, 15, 16, 17, 18, 19]

# using lambda function
add = list(map(lambda x: x + 10, num))
print(add) # [11, 12, 13, 14, 15, 16, 17, 18, 19]