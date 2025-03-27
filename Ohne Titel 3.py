const gameBoard = document.getElementById("game-board");
const criminalsMoneyText = document.getElementById("criminals-money");
const policePositionText = document.getElementById("police-position");

let criminalsMoney = 0;
let policePosition = { x: 0, y: 0 };
let criminalPosition = { x: 2, y: 2 };

// Spielfeld generieren
for (let i = 0; i < 25; i++) {
  const cell = document.createElement("div");
  gameBoard.appendChild(cell);
}

// Bewege Kriminellen
document.getElementById("move-criminal").addEventListener("click", () => {
  criminalPosition.x += 1; // Beispiel für Bewegung
  updateGame();
});

// Polizei-Aktion
document.getElementById("police-action").addEventListener("click", () => {
  policePosition.x += 1; // Beispiel für Polizeiaktion
  updateGame();
});

// Update der Anzeige
function updateGame() {
  criminalsMoneyText.textContent = `Geld der Kriminellen: $${criminalsMoney}`;
  policePositionText.textContent = `Polizei Position: ${policePosition.x}, ${policePosition.y}`;
}