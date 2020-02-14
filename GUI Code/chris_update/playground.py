import random
# # n = 2
# # for i in range(n): 
# #     for j in range(l):
# #         eval('data_'+str(i))[j] = some_length_based_maths[j]


# # for i in range(3):
# # ls = [12, 52, 235, 23, 35]
# # a = int(random.sample(ls, 1))
# # print a

# # b = ('a' + str(129))
# # print b

# st = "hello"
# # print st[1:3:2]


# qn = 3
# alist = []
# for i in range(1, qn + 1):
#     alist.append('q' + str(i))

# print alist
q1 = 1
q2 = 2
q3 = 3
ls = [q1, q2, q3]

def best():
    random.shuffle(ls)
    for elem in ls: print(elem)

best()

