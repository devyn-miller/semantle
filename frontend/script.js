function makeGuess() {
    const word = document.getElementById('guessInput').value;
    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: word })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = `Similarity: ${data.similarity}, Rank: ${data.rank}`;
    });
}