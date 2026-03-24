text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

n = len(text)
m = len(pattern)

count = 0

for i in range(n - m + 1):
    j = 0
    while j < m and text[i + j] == pattern[j]:
        j += 1

    if j == m:
        count += 1

print("Total occurrences:", count)
