text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

n = len(text)
m = len(pattern)

found = False

for i in range(n - m + 1):
    for j in range(m):
        if text[i + j] != pattern[j]:
            break
    if j == m - 1 and text[i + j] == pattern[j]:
        found = True
        break

if found:
    print("Pattern found")
else:
    print("Pattern not found")