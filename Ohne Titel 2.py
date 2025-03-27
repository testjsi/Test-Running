body {
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
}

#game-container {
  text-align: center;
  width: 80%;
}

#game-board {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 1fr);
  gap: 5px;
  margin: 20px;
}

#game-board div {
  width: 50px;
  height: