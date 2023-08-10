# Problem 1
count = 0
vowels = ['a','e','i','o','u']

for char in s:
    if char in vowels:
        count += 1
 
print(count)

# Problem 2
count = 0

try:
    for i in range(len(s)):
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            count += 1
    print(count)
except:
    print(count)

# Problem 3
def alphabetical (string):
    longest_count = 0
    substring = string[0]
    longest_substring = string[0]
    for i in range(len(string) - 1):
        if ord(string[i+1]) >= ord(string[i]):
            substring += string[i+1]
            if len(substring) > longest_count:
                longest_count = len(substring)
                longest_substring = substring
        else:
            substring = string[i+1]
        i += 1
    print(longest_substring)

