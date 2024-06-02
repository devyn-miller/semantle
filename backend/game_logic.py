from word2vec_model import get_similarity, get_rank
import random

class SemantleGame:
    def __init__(self, word_list):
        self.secret_word = random.choice(word_list)  # Dynamically set from a list of words
        self.guesses = []

    def make_guess(self, word):
        similarity = get_similarity(word, self.secret_word)
        rank = get_rank(word, self.secret_word)
        guess_info = {
            "word": word,
            "similarity": similarity,
            "rank": rank
        }
        self.guesses.append(guess_info)
        return guess_info

    def game_status(self):
        if self.guesses and self.guesses[-1]['rank'] == 1000:
            return "Congratulations! You've guessed the secret word."
        return "Keep guessing!"

# Example usage:
word_list = ['example', 'test', 'word', 'play', 'game']
game = SemantleGame(word_list)
print(game.make_guess('test'))
print(game.game_status())