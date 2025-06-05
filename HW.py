# number = int (input("Enter a number:"))

# if number % 2 ==0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

words = []
for i in range(3):
    word = input (f" Enter word {i + 1}:")
    words .append(word)

    print("\nlength of  word:" , words)

print ("\nLength of each word:")
for word in words:
    print (f"The word '{word}' has {len(word)} characters.")

