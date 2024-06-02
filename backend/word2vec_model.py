from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('path/to/word2vec.bin', binary=True)

def get_similarity(word1, word2):
    return model.similarity(word1, word2) * 100

def get_rank(word, target_word):
    # Normalize words to lowercase to handle case insensitivity
    word = word.lower()
    target_word = target_word.lower()
    
    # Check if the guessed word is the target word
    if word == target_word:
        return 1000  # Highest rank indicating a match
    
    # Get the list of words most similar to the target word
    most_similar_words = model.most_similar(target_word, topn=1000)
    
    # Check if the guessed word is in the top 1000 similar words
    for rank, (similar_word, _) in enumerate(most_similar_words, start=1):
        if similar_word == word:
            return rank
    
    return "????"  # Return "????" if the word is not in the top 1000
