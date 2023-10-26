
text = "The February TIOBE Index of the most popular programming languages is out, and while the work going on in the background of TIOBE calculations has changed, not much has shifted in the way of rankings."

words = text.split()

filtered_words = [word for word in words if len(word) > 5]

print(filtered_words)