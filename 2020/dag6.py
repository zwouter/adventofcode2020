# Part 1
# f = open("data6").read().split("\n\n")
# count = 0
# for x in f:
#     s = set()
#     for i in x.replace("\n",""):
#         s.add(i)
#     count += len(s)
#
# print(count)

# Part 2
# f = open("data6").read().split("\n\n")
# count = 0
# for x in f:
#     l = len(x.split("\n"))
#     s = {}
#     for i in x.replace("\n", ""):
#         if i in s:
#             s[i] += 1
#         else:
#             s[i] = 1
#     for v in s.values():
#         if v == l:
#             count += 1
# print(count)

# Oneliner
print(sum(sum(v==x.count("\n")+1for v in{i:x.count(i)for i in x}.values())for x in open("d").read().split("\n\n")))
