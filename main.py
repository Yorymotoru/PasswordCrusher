import random

password = input("Enter your string: ")
n = int(input("Enter the number of output lines: "))
k = int(input("Enter the number of sufficient ones: "))

arr = []
que = []
for i in range(n):
    arr.insert(i, "")

for i in range(len(password)):
    que.clear()
    for j in range(n):
        que.insert(j, j)
    for j in range(n - k + 1):
        ki = random.randrange(0, len(que), 1)
        arr[que[ki]] += password[i]
        que.pop(ki)
    for j in range(len(que)):
        arr[que[j]] += "*"

print(arr)
