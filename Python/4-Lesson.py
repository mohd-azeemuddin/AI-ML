# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# for i in range(0,51):
#     if i % 5 == 0:
#         print(i)

# total = 0
# for i in range(1,101):
#     total += i
# print(total)

# text = input("Enter the text:").lower()
# vowel = "aeiou"
# vowel_count = 0
# for ch in text:
#     if ch in vowel:
#         vowel_count += 1
# print(vowel_count)

secret = 7

while True:
    guess = int(input("Guess the secret number: "))
    
    if guess == secret:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")