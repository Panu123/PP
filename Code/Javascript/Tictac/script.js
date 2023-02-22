const board = document.querySelector('.board');
const squares = Array.from(document.querySelectorAll('.square'));
let currentPlayer = 'X';
let gameOver = false;

// add click event listener to each square
squares.forEach(square => {
    square.addEventListener('click', () => {
        if (!gameOver && !square.textContent) {
            square.textContent = currentPlayer;
            checkForWinner();
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }
    });
});

function checkForWinner() {
    const winningCombos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    for (let i = 0; i < winningCombos.length; i++) {
        const [a, b, c] = winningCombos[i];
        if (squares[a].textContent &&
            squares[a].textContent === squares[b].textContent &&
            squares[a].textContent === squares[c].textContent) {
            alert(`${currentPlayer} wins!`);
            gameOver = true;
            break;
        }
    }

    // check for tie
    if (!gameOver && squares.every(square => square.textContent)) {
        alert("It's a tie!");
        gameOver = true;
    }
}

//add new game button and score board