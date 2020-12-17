n = int(input("Enter the number of input lines: "))
lines = []
for i in range(n):
    lines.append(input())

password = ""

for i in range(len(lines[0])):
    for j in range(len(lines)):
        if lines[j][i] != '*':
            password += lines[j][i]
            break

print(password)