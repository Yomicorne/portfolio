// game.js

document.addEventListener("DOMContentLoaded", function () {
    const gameElement = document.getElementById("game");
    const scoreElement = document.getElementById("score");

    let score = 0;

    gameElement.addEventListener("click", function () {
        score++;
        updateScore();
    });

    function updateScore() {
        scoreElement.textContent = `Score: ${score}`;
    }
});
