#1
nums = list(map(int, input().split()))
squares = map(lambda x: x*x, nums)
print(sum(squares))

#2
nums = list(map(int, input().split()))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(len(evens))

#3
words = input().split()
for i, w in enumerate(words):
    print(f"{i}:{w}", end=" ")

#4
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dot = sum(x * y for x, y in zip(a, b))
print(dot)

#5
s = input()
vowels = "aeiouAEIOU"
if any(ch in vowels for ch in s):
    print("Yes")
else:
    print("No")

#6
nums = list(map(int, input().split()))
if all(x >= 0 for x in nums):
    print("Yes")
else:
    print("No")

#7
words = input().split()
longest = max(words, key=len)
print(longest)

#8
nums = list(map(int, input().split()))
unique_nums = sorted(set(nums))
print(*unique_nums)

#9
keys = input().split()
values = input().split()
d = dict(zip(keys, values))
query = input()
if query in d:
    print(d[query])
else:
    print("Not found")

#10
nums = list(map(int, input().split()))
count = sum(map(bool, nums))
print(count)
