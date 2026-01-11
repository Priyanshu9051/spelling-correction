from textblob import TextBlob
# take input from user
user_input = input("Enter words (separated by space): ")

words = user_input.split()
corrected_words = []

for word in words:
    corrected_words.append(TextBlob(word))

print("Wrong words:", words)
print("Corrected Words are:")
for word in corrected_words:
    print(word.correct())
