<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cayo Perico - Raubüberfall</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="game-container">
    <h1>Cayo Perico - Raubüberfall</h1>
    <div id="game-board">
      <!-- Hier kommt das Spielfeld -->
    </div>
    <div id="controls">
      <button id="move-criminal">Kriminellen Bewegen</button>
      <button id="police-action">Polizei Aktion</button>
    </div>
    <div id="info-panel">
      <p id="criminals-money">Geld der Kriminellen: $0</p>
      <p id="police-position">Polizei Position: X, Y</p>
    </div>
  </div>

  <script src="game.js"></script>
</body>
</html>