raw_feedback = "   Great product! I loved the packaging and delivery was fast.   "

# strip() – Remove extra spaces
clean_feedback = raw_feedback.strip()
print("Cleaned Feedback:", clean_feedback)

#  lower(), upper(), capitalize()
print("Lowercase:", clean_feedback.lower())        # useful for keyword search
print("Uppercase:", clean_feedback.upper())        # for emphasis
print("Capitalized:", clean_feedback.capitalize()) # first letter capitalized

#  in – Check if a word exists
if "delivery" in clean_feedback.lower():
    print("Delivery mentioned in feedback.")

# replace() – Replace words
updated_feedback = clean_feedback.replace("fast", "quick")
print("Updated Feedback:", updated_feedback)

#  split() – Convert sentence to words
words = clean_feedback.split()
print("Words in feedback:", words)

# join() – Join words into a sentence (after removing punctuation)
joined = " ".join(words)
print("Joined back:", joined)

#  count() – Count occurrences
print("Number of times 'and' appears:", clean_feedback.count("and"))

#  find() – Find position of a word
position = clean_feedback.find("packaging")
print("Position of 'packaging':", position)
