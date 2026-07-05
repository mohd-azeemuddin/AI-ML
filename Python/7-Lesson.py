paragraph = input("Enter the paragraph: ")
print(len(paragraph))

print(len(paragraph.split()))

uppercase_count = 0
for ch in paragraph:
    if ch.isupper():
        uppercase_count += 1
print("Uppercase letters:", uppercase_count)

lowercase_count = 0
for ch in paragraph:
    if ch.islower():
        lowercase_count += 1

print("Lowercase letters:", lowercase_count)

vowels = "aeiouAEIOU"
vowel_count = 0
for char in paragraph:
    if char in vowels:
        vowel_count += 1
print("Vowel count:", vowel_count)