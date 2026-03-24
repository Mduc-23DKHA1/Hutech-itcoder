s = str(input())
vowel = ['a','e','i','o','u']
count = 0
for i in s.lower():
    count += 1 if i in vowel else 0
print(count)