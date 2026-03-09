import nltk

def spelling_correction(word1, word2):
    # edit_distance is a built-in function in nltk
    distance = nltk.edit_distance(word1, word2)
    
    print(f"Word 1: {word1}")
    print(f"Word 2: {word2}")
    print(f"Edit Distance: {distance}")

# Example from the exam paper
spelling_correction("nature", "creature")
