import sys

n = int(sys.stdin.readline().split()[0])

words = []

for line in sys.stdin:
    for word in line.split():
        words.append(word)
for word in words:
    if len(word) > 10:
        print(word[0]+ str(len(word) - 2) + word[-1])
    else:
        print(word)