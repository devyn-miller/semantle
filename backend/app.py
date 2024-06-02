from flask import Flask, request, jsonify
from game_logic import SemantleGame

app = Flask(__name__)
game = SemantleGame()

# Example word list
# word_list = ['example', 'test', 'word', 'play', 'game']
# game = SemantleGame(word_list)

@app.route('/guess', methods=['POST'])
def guess():
    word = request.json.get('word')
    response = game.make_guess(word)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)