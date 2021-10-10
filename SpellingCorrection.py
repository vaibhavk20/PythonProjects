from textblob import TextBlob
words = ["Data Scence", "Mahine Learnin","pley"]
# words = "data scence is tha "
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")